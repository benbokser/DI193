# 🌟 Exercise 2: Working with JSON

# Instructions:

# Using the follow code:



# Step 1: Load the JSON string

#     Import the json module.
#     Use json.loads() to parse the JSON string into a Python dictionary.
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
data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
#     Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
#     Print the value of the “salary” key.
salary = data['company']['employee']['payable']['salary']
print(salary)


# Step 3: Add the “birth_date” key
#     Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
#     Replace "YYYY-MM-DD" with an actual date.
data['company']['employee']['birth_date'] = '1990-05-15'

# Step 4: Save the JSON to a file

#     Open a file in write mode ("w").
#     Use json.dump() to write the modified dictionary to the file in JSON format.
#     Use the indent parameter to make the JSON file more readable.
with open("employee.json", "w") as f:
    json.dump(data, f, indent=2)

if __name__ == '__main__':
    with open("employee.json", "r") as f:
        loaded = json.load(f)

    print(loaded)