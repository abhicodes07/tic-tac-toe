import random
# import time 
# import array
import numpy as np 

# Assigning symbols to each player globally
PLAYER = 'X'
COMPUTER = 'O'

# setting up board using numpy 2d array
board = np.zeros([3, 3], dtype=str)

# assigning empty blocks on board
def setBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            board[i][j] = ' '

# printing board
def printBoard():
    print(f"{board[0][0]}  |  {board[0][1]}| {board[0][2]}")
    print("---|---|---")

    print(f"{board[1][0]}  |  {board[1][1]}| {board[1][2]}")
    print("---|---|---")

    print(f"{board[2][0]}  |  {board[2][1]}| {board[2][2]}")
    print()

# checking if there's any free space on the board
def checkfreeSpace():
    emptyblock = 9
    for i in range(3):
        for j in range(3):
            if board[i, j] != ' ':
                emptyblock -= 1
    print(f"Emptyblocks left: {emptyblock}")
    return(emptyblock)

# Player moves on the board
def playerMove():
    r = int(input("Enter the row #0-3: "))
    c = int(input("Enter the columun #0-3: "))
    if board[r][c] != ' ':
        print("Invalid Move, Try again: ")

    while board[r][c] == ' ':
            board[r][c] = PLAYER
            break
def computerMove():
    
    print("computer turn: ")
    r = random.randint(0, 2)
    print(f"Row: {r}")
    c = random.randint(0, 2)
    print(f"Column: {c}")
    
    if checkfreeSpace() >  0:
        if board[r][c] != ' ':
            print("Invalid move: ")
            computerMove()

        else: 
            while board[r][c] == ' ':
                board[r][c] = COMPUTER
                break
    else:
        print("w")
def checkWinner():
    pass
def printWinner():
    pass

if __name__ == "__main__":
    setBoard()
    while checkfreeSpace() != 0:
        printBoard()
        playerMove()
        computerMove()



