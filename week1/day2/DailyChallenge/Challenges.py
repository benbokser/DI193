# Instructions:
# Challenge 1: Multiples of a Number
# 1. Ask the user for two inputs:

#     A number (integer).
#     A length (integer).
number = int(input('Type an integer.'))
length = int(input('Type another integer for the length of multiples.'))
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.
list1 = []
for i in range(1,length+1):
    list1.append(number * i)
print(list1)

# Challenge 2: Remove Consecutive Duplicate Letters


# Key Python Topics:

#     input() function
#     Strings and string manipulation
#     Loops (for or while)
#     Conditional statements (if)


# Instructions:

# 1. Ask the user for a string.
str1 = input('Provide a string.')
# 2. Write a program that processes the string to remove consecutive duplicate letters.
list1 = []
for i in range(len(str1)):
    if i == 0:
        list1.append(str1[0])
    if str1[i] != list1[-1]:
        list1.append(str1[i])
#     The new string should only contain unique consecutive letters.
#     For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
str2 = ''.join(list1)
# 3. The program should print the modified string.
print(str2)