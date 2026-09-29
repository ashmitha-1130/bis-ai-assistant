import json
from sentence_transformers import SentenceTransformer

INPUT_FILE = "data/bis_sources.json"
OUTPUT_FILE = "data/bis_embeddings.json"

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

print("Loading multilingual embedding model...")
model = SentenceTransformer(MODEL_NAME)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Creating embeddings for {len(data)} BIS records...")

texts = [item["content"] for item in data]
embeddings = model.encode(texts, normalize_embeddings=True)

output = []

for item, embedding in zip(data, embeddings):
    output.append({
        "title": item["title"],
        "content": item["content"],
        "source": item["source"],
        "url": item["url"],
        "embedding": embedding.tolist()
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False)

print(f"Saved {len(output)} embeddings to {OUTPUT_FILE}")
print("Embedding model:", MODEL_NAME)
