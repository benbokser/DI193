# Exercise 1: Bank Account
# Instructions

# Part I:

#     Create a class called BankAccount that contains the following attributes and methods:
#         balance - (an attribute)
#         __init__ : initialize the attribute
#         deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
#         withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive

#         username
#         password
#         authenticated (False by default)
class BankAccount:
    def __init__(self, username, password, authenticated=False):
        self.username = username
        self.password = password
        self.authenticated = authenticated
        self.balance = 0
    def deposit(self, amount: int):
        if self.authenticated == False:
            raise Exception('Not authenticated!')
        elif amount < 0:
            raise Exception('Non-positive deposit!')
        else:
            self.balance += amount
    def withdraw(self, amount):
        if self.authenticated == False:
            raise Exception('Not authenticated!')
        elif amount < 0:
            raise Exception('Non-positive deposit!')
        else:
            self.balance -= amount
    def authenticate(self,username,password):
        if username == self.username and password == self.password:
            self.authenticated = True
acct1 = BankAccount('user1', 1234)
acct1.authenticate('user1', 1234)
acct1.deposit(800)
acct1.withdraw(50)
print(acct1.balance)
# Part II : Minimum balance account
#     Create a MinimumBalanceAccount that inherits from BankAccount.
#     Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
#     Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.
class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, authenticated=False, minimum_balance=0):
        super().__init__(username, password, authenticated)
        self.balance = 0
        self.minimum_balance=minimum_balance
    def withdraw(self, amount):
        if amount < 0:
            raise Exception('Non-positive deposit!')
        elif self.balance - amount < self.minimum_balance:
            raise Exception('Withdrawal forbidden: would take balance below minimum balancde.')
        else:
            self.balance -= amount
    

# Part III: Expand the bank account class

#     Add the following attributes to the BankAccount class:
#         username
#         password
#         authenticated (False by default)

#     Create a method called authenticate. This method should accept 2 strings : a username and a password. If the username and password match the attributes username and password the method should set the authenticated boolean to True.

#     Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception


# Part IV: BONUS Create an ATM class

#     __init__:
#         Accepts the following parameters: account_list and try_limit.

#         Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
#         Hint: isinstance()

#         Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2.
#         Hint: Check out this tutorial

#         Sets attribute current_tries = 0

#         Call the method show_main_menu (see below)

#     Methods:
#         show_main_menu:
#             This method will start a while loop to display a menu letting a user select:
#                 Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
#                 Exit.

#         log_in:
#             Accepts a username and a password.

#             Checks the username and the password against all accounts in account_list.
#                 If there is a match (ie. use the authenticate method), call the method show_account_menu.
#                 If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.

#         show_account_menu:
#             Accepts an instance of BankAccount or MinimumBalanceAccount.
#             The method will start a loop giving the user the option to deposit, withdraw or exit.


# One Last Thing: Good luck!