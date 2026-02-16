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