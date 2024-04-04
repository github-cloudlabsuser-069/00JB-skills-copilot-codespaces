# write a tic tac toe game in python

# 1. create a 3x3 board
# 2. create a function to print the board
# 3. create a function to check if the game is over
# 4. create a function to check if a player has won
# 5. create a function to check if a player has won
# 6. create a function to check if a player has won
# 7. create a function to check if a player has won
# 8. create a function to check if a player has won

# Tic Tac Toe Game

# Create a 3x3 board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if the game is over
def is_game_over():
    # Check for a draw
    if all(all(cell != ' ' for cell in row) for row in board):
        return True
    # Check for a win
    if any(all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row) for row in board):
        return True
    if any(all(board[i][j] == 'X' for i in range(3)) or all(board[i][j] == 'O' for i in range(3)) for j in range(3)):
        return True
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][i] == 'O' for i in range(3)):
        return True
    if all(board[i][2-i] == 'X' for i in range(3)) or all(board[i][2-i] == 'O' for i in range(3)):
        return True
    return False

# Function to check if a player has won
def has_player_won(player):
    # Check rows
    if any(all(cell == player for cell in row) for row in board):
        return True
    # Check columns
    if any(all(board[i][j] == player for i in range(3)) for j in range(3)):
        return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Main game loop
current_player = 'X'
while not is_game_over():
    print_board()
    print(f"Player {current_player}'s turn")
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))
    if board[row][col] == ' ':
        board[row][col] = current_player
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Invalid move. Try again.")

# Game over
print_board()
if has_player_won('X'):
    print("Player X wins!")
elif has_player_won('O'):
    print("Player O wins!")
else:
    print("It's a draw!")
