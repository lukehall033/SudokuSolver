#!/usr/bin/env python3

#Solves a given sudoku board using backtracking algorithm

testBoard = [[6, 0, 0, 1, 0, 8, 2, 0, 3],
             [0, 2, 0, 0, 4, 0, 0, 9, 0],
             [8, 0, 3, 0, 0, 5, 4, 0, 0],
             [5, 0, 4, 6, 0, 7, 0, 0, 9],
             [0, 3, 0, 0, 0, 0, 0, 5, 0],
             [7, 0, 0, 8, 0, 3, 1, 0, 2],
             [0, 0, 1, 7, 0, 0, 9, 0, 6],
             [0, 8, 0, 0, 3, 0, 0, 2, 0],
             [3, 0, 2, 9, 0, 4, 0, 0, 5]]

def print_board(board):
    print("")
    for i in range(9):
        for j in range(9):
            if (j == 2 or j == 5):
                print(board[i][j], end=" | ")
            else:
                print(board[i][j], end=" ")
        print("")
        if (i == 2 or i == 5):
            print("------+-------+------")
    print("")

def runSolve(board):
    try:
        solve(0, 0, board)
    except Exception as e:
        print("Could not solve: " + str(e))
        return
    return board

def valid_placement(x, y, board):
        num = board[x][y]
        for i in range(9):
            if (i == x):
                continue
            elif (board[i][y] == num):
                return False
        for j in range(9):
            if (j == y):
                continue
            elif (board[x][j] == num):
                return False
        m, k = (x // 3) * 3, (y // 3) * 3
        for f in range(3):
            for n in range(3):
                if (m + f == x and n + k == y):
                    continue
                elif (board[m+f][n+k] == num):
                    return False
        return True

def solve(x, y, board):
    if (x == 8 and y == 9):
        return True
    if (y > 8):
        y = 0
        x += 1
    while (board[x][y] != 0):
        y += 1
        if (x == 8 and y == 9):
            return True
        if (y == 9):
            y = 0
            x += 1
    for i in range(1, 10):
        board[x][y] = i
        if (valid_placement(x, y, board)):
            if (solve(x, y+1, board)):
                return True
    board[x][y] = 0
