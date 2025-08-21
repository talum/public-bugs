#!/usr/bin/env python3
"""
Tic Tac Toe Game in Python
A simple command-line implementation of the classic tic-tac-toe game.
"""

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'
    
    def display_board(self):
        """Display the current state of the board."""
        print("\n Current Board:")
        print(" {} | {} | {} ".format(self.board[0], self.board[1], self.board[2]))
        print("-----------")
        print(" {} | {} | {} ".format(self.board[3], self.board[4], self.board[5]))
        print("-----------")
        print(" {} | {} | {} ".format(self.board[6], self.board[7], self.board[8]))
        print("\n Positions:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print()
    
    def make_move(self, position):
        """Make a move on the board if the position is valid."""
        if position < 1 or position > 9:
            return False
        if self.board[position - 1] != ' ':
            return False
        
        self.board[position - 1] = self.current_player
        return True
    
    def check_winner(self):
        """Check if there's a winner."""
        # Winning combinations
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for pattern in win_patterns:
            if (self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] 
                and self.board[pattern[0]] != ' '):
                return self.board[pattern[0]]
        return None
    
    def is_board_full(self):
        """Check if the board is full."""
        return ' ' not in self.board
    
    def switch_player(self):
        """Switch the current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_user_input(self):
        """Get valid input from the user."""
        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter position (1-9): "))
                if 1 <= position <= 9:
                    return position
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Please enter a valid number.")
    
    def play(self):
        """Main game loop."""
        print("Welcome to Tic Tac Toe!")
        print("Players take turns placing X and O on the board.")
        print("Enter a number (1-9) to place your mark in that position.")
        
        while True:
            self.display_board()
            
            # Get player move
            position = self.get_user_input()
            
            # Try to make the move
            if not self.make_move(position):
                print("That position is already taken! Try again.")
                continue
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"🎉 Player {winner} wins!")
                break
            
            # Check for tie
            if self.is_board_full():
                self.display_board()
                print("It's a tie! 🤝")
                break
            
            # Switch players
            self.switch_player()


def main():
    """Main function to start the game."""
    while True:
        game = TicTacToe()
        game.play()
        
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y' and play_again != 'yes':
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()