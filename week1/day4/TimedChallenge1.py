# Count occurence

# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

# String: Programming is cool!
# Character: o
# 3


# String: This is a great example
# Character: y
# 0
def count_occurence(str1, ch1):
    counter = 0
    for i in str1:
        if i == ch1:
            counter +=1
    return counter

print(count_occurence('Programming is cool', 'o'))
