import json

# Json string -> Python dict (loads = load from string)

# WHEN TO USE:
# Use these when you get JSON from an API response or need to send JSON in a request.

json_string = '{"name": "Alice", "age": 30, "languages": ["Python", "JavaScript"]}'
data = json.loads(json_string)

print(f"Type {type(data)}")
print(f"Name: {data['name']}")
print(f"Languages: {data['languages']}")
print()

person = {"name": "Bob", "age": 25, "active": True, "score": None}

ugly = json.dumps(person)
print(f"Ugly:   {ugly}")

pretty = json.dumps(person, indent=2)
print(f"Pretty:\n{pretty}")
