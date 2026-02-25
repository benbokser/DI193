import json

student_data = {"name": "Charlie", "grades": [85, 92, 78, 95], "graduated": False}

# WHEN TO USE:
# Use these when you're reading from or writing to a .json file on disk.

# Write Python dic -> Json file (dump = dump to file)
with open("student.json", "w") as f:
    json.dump(student_data, f, indent=2)

# Read JSON file -> Python dict (load = load from file)
with open("student.json", "r") as f:
    loaded = json.load(f)

print(f"Loaded: {loaded}")
print(f"Name: {loaded['name']}")
print(f"Average grade: {sum(loaded['grades']) / len(loaded['grades'])}")
