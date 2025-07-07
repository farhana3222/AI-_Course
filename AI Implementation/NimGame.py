def is_winner(stones, is_ai):
    # Returns True if there are no stones left and it's NOT the AI's turn 
    return stones == 0 and not is_ai

def minimax(stones, is_ai):
    if is_winner(stones, is_ai):
        # If the game is over, return 1 if AI won, else -1 if human won
        return 1 if is_ai else -1

    if is_ai:
        best_score = -float('inf')  # AI tries to maximize the score
        for move in range(1, 4):  # Try moves of 1, 2, or 3 stones
            if stones >= move:
                score = minimax(stones - move, False)  # Simulate the human's move
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')  # Human tries to minimize the score from AI’s perspective
        for move in range(1, 4):
            if stones >= move:
                score = minimax(stones - move, True)  # Simulate the AI's next move
                best_score = min(best_score, score)
        return best_score

def ai_move(stones):
    best_score = -float('inf')
    best_move = 1
    for move in range(1, 4):
        if stones >= move:
            score = minimax(stones - move, False)  # Evaluate the outcome if AI takes this move
            if score > best_score:
                best_score = score
                best_move = move  # Store the move with the best possible outcome
    return best_move

def play_nim():
    stones = 10  # Initial number of stones
    print(" Welcome to the Nim Game!")
    print("There are", stones, "stones in the pile.")
    print("Whoever picks the last stone wins.")

    is_human_turn = True  # Human starts the game

    while stones > 0:
        print("\nStones left:", stones)
        if is_human_turn:
            while True:
                try:
                    move = int(input("Your turn (Pick 1-3 stones): "))
                    if 1 <= move <= 3 and move <= stones:
                        break  # Valid move
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            move = ai_move(stones)  # AI chooses its move
            print(" AI picks", move, "stones.")

        stones -= move  # Reduce the number of stones
        is_human_turn = not is_human_turn  # Switch turn

    # Game over: check who made the last move
    if is_human_turn:
        print(" AI wins! Better luck next time.")
    else:
        print(" You win! Great job.")

# Only run the game if this file is executed directly
if __name__ == "__main__":
    play_nim()
