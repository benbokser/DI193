# Instructions:

# 1. Ask for User Input:

#     The string must be exactly 10 characters long.
str1 = input('Type a 10-character string:')
# 2. Check the Length of the String:

#     If the string is less than 10 characters, print: "String not long enough."
#     If the string is more than 10 characters, print: "String too long."
#     If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
if len(str1) < 10:
    print('String not long enough.')
elif len(str1) > 10:
    print('String too long.')
elif len(str1) == 10:
    print('Perfect string')
# 3. Print the First and Last Characters:
#     Once the string is validated, print the first and last characters.
#print(f'Your string starts with {str1[0]} and ends with {str1[-1]}.')
    print(str1[0])
    print(str1[-1])
# 4. Build the String Character by Character:

#     Using a for loop, construct and print the string character by character.
# Start with the first character, then the first two characters, and so on,
# until the entire string is printed.

# Hint: You can create a loop that goes through the string, adding one character at a time, 
# and print it progressively.

# Example:

# Alt text
    str2 = ''
    for letter in str1:
        str2 += letter
        print(str2)



# 5. Bonus: Jumble the String (Optional)
    print('Now jumbling the string')
    import random
    list1 = list(str1)
    random.shuffle(list1)
    str3 = ''.join(list1)
    print(str3)
#     As a bonus, try shuffling the characters in the string and print the newly jumbled string.

# Hint: You can use the random.shuffle function to shuffle a list of characters.
