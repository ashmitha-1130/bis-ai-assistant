import json
import re
import numpy as np
import ollama
from sentence_transformers import SentenceTransformer



# Config
OLLAMA_MODEL = "llama3.2:3b"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SIMILARITY_THRESHOLD = 0.60

# Language detection

def detect_language(text):

    marathi_words = [
        "मी", "माझा", "माझे", "माझ्या", "आम्ही", "आमचा", "आमचे",
        "करतो", "करते", "केले", "कुठला", "कुठले", "कुठल्या",
        "आहे", "आहेत", "यासाठी", "याबद्दल", "माझ्या उत्पादनासाठी"
    ]

    hindi_words = [
        "मैं", "मेरा", "मेरी", "मेरे", "हम", "हमारा", "हमारी",
        "करता", "करती", "करते", "कौन", "कौन सा", "कौनसा",
        "कौन सी", "क्या", "कैसे", "कैसा", "कैसी", "है", "हैं",
        "जानकारी", "मेरे उत्पाद के लिए"
    ]

    marathi_score = sum(
        word in text for word in marathi_words
    )

    hindi_score = sum(
        word in text for word in hindi_words
    )

    if marathi_score > hindi_score and marathi_score > 0:
        return "Marathi"

    if hindi_score > 0:
        return "Hindi"

    if re.search(r"[\u0A80-\u0AFF]", text):
        return "Gujarati"

    if re.search(r"[\u0C00-\u0C7F]", text):
        return "Telugu"

    if re.search(r"[\u0D00-\u0D7F]", text):
        return "Malayalam"

    if re.search(r"[\u0B80-\u0BFF]", text):
        return "Tamil"

    if re.search(r"[\u0900-\u097F]", text):
        return "Hindi"

    return "English"


# Answer generationn
def generate_answer(question, language, context):

    prompt = f"""You are a BIS assistant.

Answer ONLY from the BIS information provided.

Reply in {language}.

IMPORTANT:
Maximum 2 short sentences.
Answer naturally and clearly in the requested language.
Use simple language suitable for an industry user.
Keep technical names exactly as written in the BIS information.
Keep "BIS" exactly as "BIS".
Keep "IS" exactly as "IS".
Keep all standard numbers exactly as written, for example "IS 4250:2025".
Do not translate or rewrite technical names or standard numbers.
Do not invent facts.
Do not repeat the question.

BIS information:
{context}

Question:
{question}

Answer:"""

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    full_answer = ""

    for chunk in response:

        text = chunk["message"]["content"]

        # Collect the response without printing it here. (removing redundant responsess)
        # This prevents the answer from appearing twice.
        full_answer += text

    return full_answer.strip()

# FALLBACK (for prototype main focus - (english,hindi,marathi)

def fallback_message(language):

    messages = {

        "English":
            "I don't have enough information in my BIS knowledge base to answer that.",

        "Hindi":
            "मेरे BIS ज्ञान आधार में इस प्रश्न का उत्तर देने के लिए पर्याप्त जानकारी नहीं है।",

        "Marathi":
            "माझ्या BIS ज्ञान आधारामध्ये या प्रश्नाचे उत्तर देण्यासाठी पुरेशी माहिती नाही.",

        "Gujarati":
            "મારા BIS જ્ઞાન આધારમાં આ પ્રશ્નનો જવાબ આપવા માટે પૂરતી માહિતી નથી.",

        "Telugu":
            "నా BIS జ్ఞాన ఆధారంలో ఈ ప్రశ్నకు సమాధానం ఇవ్వడానికి తగిన సమాచారం లేదు.",

        "Tamil":
            "இந்த கேள்விக்கு பதிலளிக்க எனது BIS அறிவுத் தளத்தில் போதுமான தகவல் இல்லை.",

        "Malayalam":
            "ഈ ചോദ്യത്തിന് ഉത്തരം നൽകാൻ എന്റെ BIS വിജ്ഞാന ശേഖരത്തിൽ മതിയായ വിവരമില്ല."
    }

    return messages.get(
        language,
        messages["English"]
    )

# LOAD DATA

print("Loading embedding model...")

model = SentenceTransformer(
    EMBEDDING_MODEL
)

with open(
    "data/bis_embeddings.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)

# ASK QUESTION
question = input(
    "\nAsk your BIS question: "
).strip()

language = detect_language(
    question
)

print(
    f"\nDetected language: {language}"
)

# MULTILINGUAL SEARCH
query_embedding = model.encode(
    question,
    normalize_embeddings=True
)

# SEMANTIC SEARCH

results = []

for record in data:

    record_embedding = np.array(
        record["embedding"]
    )

    similarity = np.dot(
        query_embedding,
        record_embedding
    )

    results.append(
        (similarity, record)
    )


results.sort(
    reverse=True,
    key=lambda x: x[0]
)

# RELEVANT RESULTS

# If the top match is very strong, use only that record.
# This prevents generic BIS records from distracting the LLM.

if results and results[0][0] >= 0.65:
    top_results = [results[0]]

else:
    top_results = [
        result
        for result in results
        if result[0] >= SIMILARITY_THRESHOLD
    ][:3]



# FALLBACK IF NOTHING FOUND (dealing with hallucination)

if not top_results:

    print("\nANSWER:")

    print(
        fallback_message(language)
    )

    print(
        "\nNo sufficiently relevant BIS evidence was found."
    )

    exit()

# BUILD CONTEXT

context_parts = []

for similarity, record in top_results:

    context_parts.append(
        f"""
Title: {record["title"]}
Standard Number: {record.get("standard_number", "N/A")}
Content: {record["content"]}
Source: {record.get("source", "BIS")}
URL: {record.get("url", "N/A")}
"""
    )


context = "\n".join(
    context_parts
)


# FREE EMBEDDING MODEL MEMORY

del model

# LLM GENERATION

print("\nThinking...")

answer = generate_answer(
    question,
    language,
    context
)


# EXACT STANDARD NUMBER

standard_number = top_results[0][1].get(
    "standard_number",
    "Not identified"
)

title = top_results[0][1].get(
    "title",
    ""
)

clean_title = title

if standard_number != "Not identified":

    clean_title = clean_title.replace(
        standard_number + " - ",
        ""
    )

    clean_title = clean_title.replace(
        standard_number,
        ""
    ).strip(" -")

# FINAL ANSWER

print("\nANSWER:")

if standard_number != "Not identified":

    print(
        f"Standard: {standard_number} - {clean_title}"
    )

print(answer)


# EVIDENCE

print("\nEVIDENCE:")

for similarity, record in top_results:

    print(
        f"\n[{record['title']}]"
    )

    print(
        f"Similarity: {similarity:.3f}"
    )

    print(
        record["content"]
    )

    print(
        f"Source: {record.get('source', 'BIS')}"
    )

    print(
        f"URL: {record.get('url', 'N/A')}"
    )
