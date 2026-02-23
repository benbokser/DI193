# 🌟 Exercise 4: Family and Person Classes

# Goal:

# Practice working with classes and object interactions by modeling a family and its members.



# Instructions:

# Step 1: Create the Person Class
#     Define a Person class with the following attributes:
#     first_name
#     age
#     last_name (string, should be initialized as an empty string)
#     Add a method called is_18():
#     It should return True if the person is 18 or older, otherwise False.
class Person:
    def __init__(self, first_name: str, age: int):
        self.first_name = first_name
        self.age = age
        self.last_name = ''
    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
# Step 2: Create the Family Class
#     Define a Family class with:
#         A last_name attribute
#         A members list that will store Person objects (should be initialized as an empty list)
class Family:
    def __init__(self, last_name: str):
        self.last_name = last_name
        self.members = []

#     Add a method called born(first_name, age):
#         It should create a new Person object with the given first name and age.
#         It should assign the family’s last name to the person.
#         It should add this new person to the members list.

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
#     Add a method called check_majority(first_name):
#         It should search the members list for a person with that first_name.
#             If the person exists, call their is_18() method.
#         If the person is over 18, print:
#             "You are over 18, your parents Jane and John accept that you will go out with your friends"
#         Otherwise, print:
#             "Sorry, you are not allowed to go out with your friends."
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18() == True:
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends.')
                else:
                    print('Sorry, you are not allowed to go out with your friends.')

#     Add a method called family_presentation():
#         It should print the family’s last name.
#         Then, it should print each family member’s first name and age.
    def family_presentation(self):
        print(f'{self.last_name} family:')
        for member in self.members:
            print(f'{member.first_name}, age {member.age}')

# Expected Behavior:
# Once implemented, your program should allow you to:
#     Create a family with a last name.
#     Add members to the family using the born() method.
#     Use check_majority() to see if someone is allowed to go out.
#     Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.
fam1 = Family('Klein')
fam1.born('Jack', 8)
fam1.born('Amy', 20)
fam1.born('Sue', 25)

fam1.check_majority('Sue')

fam1.family_presentation()
