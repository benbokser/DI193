import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/")

print(response)
print(type(response))

# 1 - Did it work? (200 = yes)
status = response.status_code

# 2 - Give me the data as a Python dict
data = response.json()
# print(data)

# 3 - Give me the raw text (useful for debugging)
raw = response.text
# print(raw)

for user in data:
    print(f"    {user['name']} - {user['email']}")
