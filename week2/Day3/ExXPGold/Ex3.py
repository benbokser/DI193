# Exercise 3 : Regular Expression #1
# Instructions

# Hint: Use the RegEx (module)

#     Use the regular expression module to extract numbers from a string.

import re
def return_numbers(string: str):
    return ''.join(re.findall(r'\d+', string))

print(return_numbers('k5k3q2g5z6x9bn'))
