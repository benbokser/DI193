
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def display_board(board):
    board_display = f"""TIC TAC TOE
*******************
*    {board[0][0]} | {board[0][1]} | {board[0][2]}     *
*   ---|---|---    *
*    {board[1][0]} | {board[1][1]} | {board[1][2]}     *
*   ---|---|---    *
*    {board[2][0]} | {board[2][1]} | {board[2][2]}     *
*******************"""
    print(board_display)


def player_input(player):
#player will be X or 0
    print(f"Player {player}'s turn:")
    while True:
        row = input('Enter row:')
        column = input('Enter column:')
        if not (1 <= int(row) <= 3 and 1 <= int(column) <= 3):
            print('Invalid entry. Try again.')
        elif not board[int(row)-1][int(column)-1] == ' ':
            print('Cell is full. Try again.')
        else:
            board[int(row)-1][int(column)-1] = player
            break
        
    
# Step 4: Checking for a Winner

#     Create a function called check_win(board, player) to check if the current player has won.
#     The function should check all possible winning combinations (rows, columns, diagonals).
#     If a player has won, return True; otherwise, return False.
#     Think about how to check every possible winning combination.

def check_win(board, player):
    '''check if current player has won.'''
    # horizontals:
    if board[0][0] == board [0][1] == board [0][2] == player:
        return True
    elif board[1][0] == board [1][1] == board [1][2] == player:
        return True
    elif board[2][0] == board [2][1] == board [2][2] == player:
        return True
    # verticals:
    elif board[0][0] == board [1][0] == board [2][0] == player:
        return True
    elif board[0][1] == board [1][1] == board [2][1] == player:
        return True
    elif board[0][2] == board [1][2] == board [2][2] == player:
        return True
    # diagonals:
    elif board[0][0] == board [1][1] == board [2][2] == player:
        return True
    elif board[0][2] == board [1][1] == board [2][0] == player:
        return True
    else:
        return False


# Step 5: Checking for a Tie

#     Create a function to check if the game has resulted in a tie.
#     The function should check if all positions of the board are full, without a winner.
def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    if check_win(board, 'X') == True:
        return False
    if check_win(board, 'O') == True:
        return False
    return True

# Step 6: The Main Game Loop

#     Create a function called play() to manage the game flow.
#     Initialize the game board.
#     Use a while loop to continue the game until there’s a winner or a tie.
#     Inside the loop:
#         Display the board.
#         Get the current player’s input.
#         Update the board with the player’s move.
#         Check for a winner.
#         Check for a tie.
#         Switch to the next player.
#     After the loop ends, display the final result (winner or tie).
def play():
# board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = 'X'
    while True:
        display_board(board)
        print
        player_input(current_player)
        display_board(board)
        if check_win(board, current_player):
            print(f'{current_player} won! Game Over.')
            break
        if check_tie(board):
            print('Tie! Game Over.')
            break
        if current_player == 'X':
            current_player = 'O'
        elif current_player == 'O':
            current_player = 'X'

    
play()