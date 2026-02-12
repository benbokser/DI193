#1 Declare a variable called first and assign it
# to the value "Hello World".

first = "Hello World"
#2     Write a comment that says "This is a comment."

# This is a comment.
#3     Log a message to the terminal that says "I AM A COMPUTER!"
"I AM A COMPUTER!"
#4 Write an if statement that checks if 1 is less than 2
#  and if 4 is greater than 2.
# If it is, show the message "Math is fun."
if 1<2 and 4>2:
    print("Math is fun.")
#5: Assign a variable called nope to an absence of value.
nope = None
#6: Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.
True and False
#7    Calculate the length of the string "What's my length?"

len("What's my length?")
#8 Convert the string "i am shouting" to uppercase.
"i am shouting".upper()
#9 Convert the string "1000" to the number 1000.
int("1000")
#10 Combine the number 4 with the string "real" to produce "4real".
str(4) + "real"
#11 Record the output of the expression 3 * "cool".
3*"cool"
#  12 Record the output of the expression 1 / 0.
1/0
#13 Determine the type of []
type([])
#14 Ask the user for their name, and store it in a variable called name.
name = input("What is your name?")
#15 Ask the user for a number.
#If the number is negative, show a message that says "That number is less than 0!"
#If the number is positive, show a message that says "That number is greater than 0!"
#Otherwise, show a message that says "You picked 0!

number = int(input("Pick a number."))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")
#16 Find the index of "l" in "apple".
"apple".find('l')
#17 Check whether "y" is in "xylophone".
'y' in 'xylophone'
# 18 Check whether a string called my_string is all in lowercase.
[ ]

my_string = 'abc'
my_string == my_string.lower()
humanYears = int(input("How many years ago did you get the cat and dog?"))
if humanYears == 1:
    catYears = 15
    dogYears = 15
elif humanYears == 2:
    catYears = 15+9
    dogYears = 15+9
elif humanYears > 2:
    catYears = 15+9 + 4*(humanYears - 2)
    dogYears = 15+9 + 5*(humanYears - 2)
print(f"[{humanYears},{catYears},{dogYears}]")

