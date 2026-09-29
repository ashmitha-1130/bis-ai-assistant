from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "BIS develops Indian Standards for products, processes and services."

embedding = model.encode(text)

print("Embedding created!")
print("Number of values:", len(embedding))
print("First 5 values:", embedding[:5])
