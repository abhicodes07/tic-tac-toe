import numpy as np 
# from time import sleep

class Players:
    def __init__(self, p):
        self.name = name
        self.choice = " "
        self.ponts = 0

    def choose(self):
        pass
    
    def incrementPoints(self):
        pass

class GameRound:
    def __init__(self):
        pass

    def freeSpace(self):
        pass


class StartGame:
    def __init__(self):
        self
        self.board = np.zeros([3, 3], dtype=str)

    def setBoard(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.board[i][j] = ' '

    def printtBoard(self):
        print(f"{self.board[0][0]}  | {self.board[0][1]} | {self.board[0][2]}")
        print("---|---|---")

        print(f"{self.board[1][0]}  | {self.board[1][1]} | {self.board[1][2]}")
        print("---|---|---")

        print(f"{self.board[2][0]}  | {self.board[2][1]} | {self.board[2][2]}")
        print()


    def printWinner(self):
        pass

if __name__ == "__main__":
    pass

