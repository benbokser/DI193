import json
sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
# Step 1: Parse the JSON string

# Step 2: Access and print the salary

# Step 3: Add birth_date to the employee

# Step 4: Save to employee.json

# Step 5: Read back and verify
data = json.loads(sampleJson)

print(data['company']['employee']['payable']['salary'])
data['company']['employee']['birth_date'] = '1990-05-15'

with open("employee.json", "w") as f:
    json.dump(data, f, indent=2)
    print('Modified data saved to JSON')

with open("employee.json", "r") as f:
    loaded = json.load(f)

print(loaded)