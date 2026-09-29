import json

with open("data/bis_sources.json", "r", encoding="utf-8") as file:
    bis_data = json.load(file)

print("Number of BIS records:", len(bis_data))

for record in bis_data:
    print("\nTitle:", record["title"])
    print("Category:", record["category"])