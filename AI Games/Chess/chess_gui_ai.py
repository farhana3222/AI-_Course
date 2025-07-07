import pygame
import chess
import sys

# Constants
WIDTH, HEIGHT = 480, 480
SQ_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Piece images dictionary
PIECE_IMAGES = {}

# Load piece images
def load_images():
    pieces = ['P', 'R', 'N', 'B', 'Q', 'K']
    for piece in pieces:
        PIECE_IMAGES['w' + piece] = pygame.transform.scale(pygame.image.load(f"image/w{piece}.png"), (SQ_SIZE, SQ_SIZE))
        PIECE_IMAGES['b' + piece] = pygame.transform.scale(pygame.image.load(f"image/b{piece}.png"), (SQ_SIZE, SQ_SIZE))

# Highlight selected square and possible moves
def highlight_squares(screen, board, selected_square):
    if selected_square is None:
        return
    s = selected_square
    col = chess.square_file(s)
    row = 7 - chess.square_rank(s)

    # Highlight selected square (yellow border)
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)

    # Highlight possible moves (green circles)
    for move in board.legal_moves:
        if move.from_square == selected_square:
            dest = move.to_square
            dc = chess.square_file(dest)
            dr = 7 - chess.square_rank(dest)
            center = (dc * SQ_SIZE + SQ_SIZE // 2, dr * SQ_SIZE + SQ_SIZE // 2)
            pygame.draw.circle(screen, (0, 255, 0), center, 10)

# Draw the board
def draw_board(screen, board, selected_square):
    colors = [WHITE, GRAY]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
    highlight_squares(screen, board, selected_square)
    draw_pieces(screen, board)

# Draw the pieces on the board
def draw_pieces(screen, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            piece_str = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().upper()
            screen.blit(PIECE_IMAGES[piece_str], pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Evaluation function (basic material count)
def evaluate(board):
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }
    eval = 0
    for piece in board.piece_map().values():
        value = values.get(piece.piece_type, 0)
        eval += value if piece.color == chess.BLACK else -value
    return eval

# Minimax algorithm
def minimax(board, depth, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    best_move = None
    if maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth-1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth-1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess: You vs AI")
    board = chess.Board()
    clock = pygame.time.Clock()
    load_images()

    selected_square = None
    running = True

    while running:
        draw_board(screen, board, selected_square)
        pygame.display.flip()

        if board.turn == chess.BLACK:  # AI's turn
            print("AI is thinking...")
            _, move = minimax(board, 2, True)
            if move:
                board.push(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE:
                col = event.pos[0] // SQ_SIZE
                row = 7 - (event.pos[1] // SQ_SIZE)
                square = chess.square(col, row)

                if selected_square is None:
                    if board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
