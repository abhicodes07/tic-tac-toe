import numpy as np 


PLAYER = 'X'
board = np.zeros((3, 3), dtype=str)
for i in range(3):
    for j in range(3):
        board[i][j] = '*'
print(board)
