import json
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load embedded BIS data
with open("data/bis_embeddings.json", "r", encoding="utf-8") as file:
    data = json.load(file)

question = input("\nAsk your BIS question: ")

# Convert question into an embedding
question_embedding = model.encode(question)

# Calculate similarity
results = []

for record in data:
    record_embedding = np.array(record["embedding"])

    similarity = np.dot(question_embedding, record_embedding) / (
        np.linalg.norm(question_embedding) *
        np.linalg.norm(record_embedding)
    )

    results.append((similarity, record))

# Sort by similarity
results.sort(reverse=True, key=lambda x: x[0])

print("\nMost relevant BIS information:\n")

for similarity, record in results[:3]:
    print(f"Similarity: {similarity:.3f}")
    print(f"Title: {record['title']}")
    print(f"Category: {record['category']}")
    print(f"Source: {record['source']}")
    print()