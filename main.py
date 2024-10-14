import random
from time import sleep
import numpy as np 

# Constants
# Assigning symbols to each player globally
PLAYER: str = 'X'
COMPUTER: str = 'O'
WINNER: str = ' '

# setting up board using numpy 2d array
board: int = np.zeros([3, 3], dtype=str)

# assigning empty blocks on board
def setBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            board[i][j] = ' '

# printing board
def printBoard() -> None:
    print(f"{board[0][0]}  | {board[0][1]} | {board[0][2]}")
    print("---|---|---")

    print(f"{board[1][0]}  | {board[1][1]} | {board[1][2]}")
    print("---|---|---")

    print(f"{board[2][0]}  | {board[2][1]} | {board[2][2]}")
    print()

# checking if there's any free space on the board
def checkfreeSpace() -> int:
    emptyblock = 9
    for i in range(3):
        for j in range(3):
            if board[i, j] != ' ':
                emptyblock -= 1
    print(f"Emptyblocks left: {emptyblock}")
    return(emptyblock)

# Player moves on the board
def playerMove() -> int:
    print("\n--> YOUR TURN!")
    r = int(input("Enter the row #0-3: "))
    c = int(input("Enter the columun #0-3: "))
    if board[r][c] != ' ':
        print("Invalid Move, Try again: ")

    while board[r][c] == ' ':
            board[r][c] = PLAYER
            break
    
# Computer's move 
# Generating random number i.e., the indexes of empty blocks
def computerMove() -> int:  
    print("\n--> COMPUTER TURN: ")
    r = random.randint(0, 2)
    sleep(1)
    print(f"Row: {r}")
    c = random.randint(0, 2)
    sleep(1)
    print(f"Column: {c}")

    
    if board[r][c] != ' ':
        print("Invalid move: ")
        computerMove()

    while board[r][c] == ' ':
        board[r][c] = COMPUTER
        break

# Checking winner on grid
def checkWinner() -> int:
    # Checking rows
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            print(f"Winner: {board[i][0]}\n")
            return(board[i][0])
    
    # Checking column
    for j in range(3):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j]:
            print(f"Winner: {board[0][j]}\n")
            return(board[0][j])
    
    # Checking Diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        print(f"Winner: {board[0][0]}\n")
        return(board[0][0])

    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        print(f"Winner: {board[0][2]}\n")
        return(board[0][2])
    
    else:
        print(f"Winner: {WINNER}")
        return WINNER
    
# printing winner
def printWinner(WINNER: str) -> str:
    if WINNER == PLAYER:
        print("\n-- LAST BOARD --")
        printBoard()
        print("\n -- YOU WIN! --\n")
    elif WINNER == COMPUTER:
        print("\n -- LAST BOARD --")
        printBoard()
        print("\n -- YOU LOSE! --\n")
    else:
        print("\n -- LAST BOARD --")
        printBoard()
        print("\n-- IT'S A TIE. --\n")

# Main
if __name__ == "__main__":
    setBoard()
    while WINNER == ' ' and checkfreeSpace() != 0:
        printBoard()

        playerMove()
        # if checkWinner() == ' ' 
        WINNER = checkWinner()
        if WINNER != ' ' or checkfreeSpace() == 0:
            printWinner(WINNER)
            break

        computerMove()
        WINNER = checkWinner()
        if WINNER != ' ' or checkfreeSpace() == 0:
            printWinner(WINNER)
            break


