# Instructions:

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