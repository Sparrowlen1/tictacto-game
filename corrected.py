import random

class TicTacToe:
    def __init__(self):
        # Initialize an empty board
        self.board = ["" for _ in range(9)]
        self.human_player = "X"  # Human will be X
        self.computer_player = "O"  # Computer will be O
        self.current_player = "X"  # X always goes first

    def display_board(self):
        # Display the current state of the board
        print("\n")
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print("|".join([cell if cell != "" else " " for cell in row]))
            print("-" * 5)

    def is_winner(self, player):
        # Check all winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_draw(self):
        # Check if the game is a draw (board is full and no winner)
        return all(cell != "" for cell in self.board)

    def switch_player(self):
        # Switch the current player between human and computer
        self.current_player = (
            self.computer_player if self.current_player == self.human_player else self.human_player
        )

    def human_move(self):
        # Get the human player's move
        while True:
            try:
                move = int(input(f"Player {self.human_player}, enter a position (1-9): ")) - 1
                if move < 0 or move > 8 or self.board[move] != "":
                    print("Invalid move! Try again.")
                    continue
                return move
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

    def computer_move(self):
        # Computer randomly selects an empty spot
        available_moves = [i for i, spot in enumerate(self.board) if spot == ""]
        move = random.choice(available_moves)
        print(f"Computer chooses position {move + 1}")
        return move

    def play(self):
        # Main game loop
        while True:
            self.display_board()
            
            if self.current_player == self.human_player:
                move = self.human_move()
            else:
                move = self.computer_move()

            # Place the player's move on the board
            self.board[move] = self.current_player

            # Check if the current player has won
            if self.is_winner(self.current_player):
                self.display_board()
                print(f"Player {self.current_player} wins!")
                break

            # Check if the game is a draw
            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break

            # Switch to the other player
            self.switch_player()

# Start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
