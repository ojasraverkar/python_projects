import chess
from stockfish import Stockfish

# Initialize Stockfish engine
stockfish = Stockfish(
    path=r"D:\stockfish\stockfish-windows-x86-64-avx2.exe",
    parameters={"Threads": 2, "Minimum Thinking Time": 30},
)

board = chess.Board()

def display_board():
    """Display the chessboard."""
    print(board)

def make_move(move):
    """Handle player and bot moves."""
    try:
        user_move = chess.Move.from_uci(move)
        if user_move in board.legal_moves:
            board.push(user_move)
            stockfish.set_fen_position(board.fen())
            
            if board.is_game_over():
                print("Game over!")
                print(f"Result: {board.result()}")
                return
            
            bot_move = stockfish.get_best_move()
            if bot_move:
                print(f"Bot's Move: {bot_move}")
                board.push(chess.Move.from_uci(bot_move))
                display_board()
        else:
            print("Invalid move! Please try again.")
    except ValueError:
        print("Invalid input! Enter moves in UCI format (e.g., e2e4).")

def start_game():
    """Start the chess game."""
    display_board()
    player_color = input("Choose your color (white/black): ").strip().lower()
    if player_color not in ["white", "black"]:
        print("Invalid color! Defaulting to white.")
        player_color = "white"

    # Bot makes the first move if the player chooses black
    if player_color == "black":
        stockfish.set_fen_position(board.fen())
        bot_move = stockfish.get_best_move()
        if bot_move:
            print(f"Bot's Move: {bot_move}")
            board.push(chess.Move.from_uci(bot_move))
            display_board()

    # Main game loop
    while not board.is_game_over():
        user_move = input("Your move: ").strip()
        make_move(user_move)

    print("Game over!")
    print(f"Result: {board.result()}")

# Start the game
start_game()
