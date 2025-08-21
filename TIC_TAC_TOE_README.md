# Tic Tac Toe Game

A simple command-line tic-tac-toe game implemented in Python.

## How to Play

1. Run the game:
   ```bash
   python3 tic_tac_toe.py
   ```

2. Players take turns placing X and O on a 3x3 board
3. Enter a number (1-9) to place your mark in the corresponding position:
   ```
   Positions:
   1 | 2 | 3 
   -----------
   4 | 5 | 6 
   -----------
   7 | 8 | 9 
   ```

4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins!
5. If the board fills up without a winner, it's a tie.

## Features

- ✅ Interactive command-line interface
- ✅ Input validation
- ✅ Win detection (rows, columns, diagonals)
- ✅ Tie detection
- ✅ Play again option
- ✅ Clear board display with position numbers

## Testing

Run the test script to verify functionality:
```bash
python3 test_tic_tac_toe.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Example Game

```
Welcome to Tic Tac Toe!
Players take turns placing X and O on the board.
Enter a number (1-9) to place your mark in that position.

 Current Board:
   |   |   
-----------
   |   |   
-----------
   |   |   

 Positions:
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

Player X, enter position (1-9): 5

 Current Board:
   |   |   
-----------
   | X |   
-----------
   |   |   

Player O, enter position (1-9): 1
...
```

Enjoy playing! 🎮