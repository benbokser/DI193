# Exercise 4 : Regular Expression #2
# Instructions

# Hint: Use the RegEx (module)
import re
#     Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
#         The name should contain only letters.
#         The name should contain only one space.
#         The first letter of each name should be upper cased.
def name_check():
    name = input('Provide your full name')
    pattern = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
    if re.match(pattern, name):
        print('Valid name format.')
    else:
        print("❌ Invalid name.")
        print("- Must contain only letters.")
        print("- Must have exactly one space.")
        print("- Each name must start with a capital letter.")

if __name__ == "__main__":
    name_check()