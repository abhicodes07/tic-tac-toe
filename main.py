# import random
# import time 
# import array
import numpy as np 

PLAYER = 'X'
COMPUTER = 'O'

board = np.zeros([3, 3], dtype=str)

def setBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            board[i, j] = ' '

def printBoard():
    print(f"{board[0][0]}  |  {board[0][1]}| {board[0][2]}")
    print("---|---|---")

    print(f"{board[1][0]}  |  {board[1][1]}| {board[1][2]}")
    print("---|---|---")

    print(f"{board[2][0]}  |  {board[2][1]}| {board[2][2]}")
    print()

def checkfreeSpace():
    emptyblock = 9
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                emptyblock -= 1
                
def playerMove():
    pass
def computerMove():
    pass
def checkWinner():
    pass
def printWinner():
    pass

if __name__ == "__main__":
    setBoard()
    printBoard()




