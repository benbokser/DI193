# 🌟 Exercise 3: String module
# Goal: Generate a random string of length 5 using the string module.

# Step 1: Import the string and random modules

#     Import the string and random modules.
import string
import random

# Step 2: Create a string of all letters
# Read about the strings methods HERE to find the best methods for this step
all_letters = string.ascii_letters

# Step 3: Generate a random string
#     Use a loop to select 5 random characters from the combined string.
#     Concatenate the characters to form the random string.
random_string = ''
for _ in range(5):
    random_string += random.choice(all_letters)

print(random_string)