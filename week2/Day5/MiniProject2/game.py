import random
# Step 1: Create the Game Class


# Step 2: Implement get_user_item Method

#     Create a method called get_user_item(self).
#     Ask the user to select an item (rock/paper/scissors).
class Game:
    def get_user_item(self):
        # ... code to get and validate user input ...
        while True:
            choice = input('Type your choice: rock, paper, or scissors.').lower()
            if choice not in ['rock','paper','scissors']:
                print('Invalid choice.')
                continue
            break
        # ... code to return user's choice ...
        return choice

# Step 3: Implement get_computer_item Method

#     Create a method called get_computer_item(self).
#     Randomly select an item (rock/paper/scissors).
#     Return the computer’s item.
    def get_computer_item(self):
        # ... code to generate computer's choice ...
        choice = random.choice(['rock','paper','scissors'])
        # ... code to return computer's choice ...
        return choice
    
# Step 4: Implement get_game_result Method

#     Create a method called get_game_result(self, user_item, computer_item).
#     Take user_item and computer_item as parameters.
#     Determine the result of the game based on the rules of Rock Paper Scissors.
#     Return “win”, “draw”, or “loss”.
    def get_game_result(self, user_item, computer_item):
        # ... code to determine and return game result ...
        if user_item == computer_item:
            return 'draw'
        if user_item == 'rock':
            if computer_item == 'paper':
                return 'loss'
            if computer_item == 'scissors':
                return 'win'
        if user_item == 'paper':
            if computer_item == 'rock':
                return 'win'
            if computer_item == 'scissors':
                return 'loss'
        if user_item == 'scissors':
            if computer_item == 'rock':
                return 'loss'
            if computer_item == 'paper':
                return 'win'


# Step 5: Implement play Method

#     Create a method called play(self).
#     Call get_user_item() to get the user’s choice.
#     Call get_computer_item() to get the computer’s choice.
#     Call get_game_result() to determine the result.
#     Print the outcome of the game (user’s choice, computer’s choice, result).
#     Return the result (“win”, “draw”, or “loss”) as a string.
    def play(self):
        # ... code to get user and computer choices ...
        # ... code to determine game result ...
        # ... code to print game outcome ...
        # ... code to return game result ...
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice,computer_choice)
        print(f'Your move: {user_choice}. Computer move: {computer_choice}. Game result: {result}.')
        return result
    
# #testing:
# if __name__ = '__main__':
# instance = Game()
# instance.play()












