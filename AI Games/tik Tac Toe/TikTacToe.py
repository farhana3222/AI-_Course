import math  # Importing math for using infinity values in Minimax

# Function to print the current game board
def print_board(board):
    for row in board:
        print("|".join(row))  # Print each row separated by |
        print("-" * 5)        # Print a line to separate rows visually

# Function to check if there's a winner
def check_winner(board):
    # Create all possible winning lines: rows, columns, and diagonals
    lines = board + [list(col) for col in zip(*board)] + [
        [board[i][i] for i in range(3)],               # Main diagonal
        [board[i][2 - i] for i in range(3)]            # Anti-diagonal
    ]
    for line in lines:
        if line.count('X') == 3:
            return 'X'  # Player wins
        elif line.count('O') == 3:
            return 'O'  # AI wins
    return None  # No winner yet

# Function to check if the board is full (i.e., no empty spaces left)
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm to determine the best move for the AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1  # AI wins, return positive score
    elif winner == 'X':
        return -1  # Player wins, return negative score
    elif is_full(board):
        return 0  # It's a draw

    if is_maximizing:
        best_score = -math.inf  # Initialize best score for maximizer (AI)
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # Try the move
                    score = minimax(board, depth + 1, False)  # Recursively check outcome
                    board[i][j] = ' '  # Undo the move
                    best_score = max(score, best_score)  # Keep the best score
        return best_score
    else:
        best_score = math.inf  # Initialize best score for minimizer (Player)
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Function to determine the best move for the AI using Minimax
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)  # Default move if no empty cell is found
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # Try move
                score = minimax(board, 0, False)  # Evaluate move
                board[i][j] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    move = (i, j)  # Update best move
    return move

# Main function to run the game
def main():
    # Create a 3x3 empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player (human) move
        while True:
            try:
                row = int(input("Enter your move row (0-2): "))
                col = int(input("Enter your move column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'  # Player places 'X'
                    break
                else:
                    print("That spot is taken. Try again.")
            except (IndexError, ValueError):
                print("Invalid input. Try again.")

        print_board(board)

        # Check if game has ended after player's move
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        row, col = best_move(board)
        board[row][col] = 'O'  # AI places 'O'
        print_board(board)

        # Check if game has ended after AI's move
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Entry point of the program
if __name__ == "__main__":
    main()
