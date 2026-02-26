import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response)
print(type(response))

print(response.status_code)
data = response.json()
print(response.json)
raw = response.text
#print(response.text)

print(data.keys())