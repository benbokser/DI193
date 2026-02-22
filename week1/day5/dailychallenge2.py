

#     My Courses

#     Calendar
#     Leaderboard
#     Job Offers
#         About DI
#         Terms & Conditions
#         Privacy
#         Menu
#         My Courses
#         My Achievements
#         My Trophy
#         My Diploma
#         Refer Friend
#         My Payment
#         Resume Matcher
#         P2P Rooms
#         Playground
#         My OctoHelp

#     AI-Powered Data Analytics Bootcamp - 2026 - Full Time Python Fundamentals Mini-Project Day Daily challenge : Advanced Algorithm 

# Daily challenge : Advanced Algorithm

# Last Updated: February 5th, 2026

# What You will learn :

#     Python Basics
#     Conditionals
#     Loops
#     Functions


# Instructions

# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

def sum_finder(list1, target):
    pairs = []
    for x in list1:
        if x in list1:
            if (target - x) in list1:
                pairs.append([x,target-x])
                list1.remove(x)
                list1.remove(target-x)
    return pairs

print(sum_finder(list_of_numbers, target_number))
# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

# For example

# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728
