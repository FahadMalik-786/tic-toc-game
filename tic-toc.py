# Initialize the game board with 9 empty spaces
board = [" "] * 9

# Players
current_player = "X"

# Winning positions (rows, columns, diagonals)
win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def print_board():
    """Display the current board"""
    print(f"""
     {board[0]} | {board[1]} | {board[2]} 
    ---+---+---
     {board[3]} | {board[4]} | {board[5]} 
    ---+---+---
     {board[6]} | {board[7]} | {board[8]} 
    """)

def check_win(player):
    """Check if the player has any winning combination"""
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_draw():
    """Check if the board is full (draw)"""
    return " " not in board

# Game loop
while True:
    print_board()

    # Ask player for a move
    move = input(f"Player {current_player}, choose a position (0-8): ")

    # Validate input
    if not move.isdigit() or int(move) not in range(9):
        print("❌ Invalid input. Please enter a number between 0 and 8.")
        continue

    move = int(move)

    if board[move] != " ":
        print("❌ That spot is already taken. Try again.")
        continue

    # Make the move
    board[move] = current_player

    # Check for win
    if check_win(current_player):
        print_board()
        print(f"🎉 Player {current_player} wins!")
        break

    # Check for draw
    if check_draw():
        print_board()
        print("😺 It's a draw!")
        break

    # Switch player
    current_player = "O" if current_player == "X" else "X"
