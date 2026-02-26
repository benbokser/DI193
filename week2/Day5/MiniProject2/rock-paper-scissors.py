# rock-paper-scissors.py
from game import Game
# Step 6: Implement get_user_menu_choice Function

#     Create a function called get_user_menu_choice().
#     Display the menu options (“Play a new game”, “Show scores”, “Quit”).
#     Get the user’s choice.
#     Validate the input (e.g., check if it’s one of the valid options).
#     Return the user’s choice.

def get_user_menu_choice():
    # ... code to display menu and get user choice ...
    user_choice = input("""
Rock Paper Scissors Game
Menu:
1: Play a new game
2: Show Scores
3: Quit
""")
    # ... code to validate user input ...
    if user_choice not in ['1','2','3']:
        print("Improper choice. Type 1, 2, or 3.")
    # ... code to return user choice ...
    return user_choice

# Step 7: Implement print_results Function

#     Create a function called print_results(results).
#     Take a dictionary called results as a parameter (e.g., {"win": 2, "loss": 4, "draw": 3}).
#     Print the results in a user-friendly format (e.g., “Wins: 2, Losses: 4, Draws: 3”).
#     Thank the user for playing.
def print_results(results):
    # ... code to print results in a user-friendly way ...
    print(f'Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}')
    # ... code to thank user ...
    print('Thanks for playing!')

# Step 8: Implement main Function

#     Create a function called main().
#     Pepeatedly show the menu until the user chooses to exit.
#     Call get_user_menu_choice() to get the user’s choice.
#     If the user chooses to play a game:
#         Create a Game object.
#         Call the play() method of the Game object.
#         Store the result of the game in a dictionary (e.g., results).
#     If the user chooses to exit:
#         Call print_results() to display the game summary.
#         Exit the program.
def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        if choice == '2':
            print_results(results)
        if choice == '3':
            print_results(results)
            break
    # ... code to call all the related functions depending on the user's choice.


if __name__ == "__main__":
    main()








