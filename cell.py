from random import randint

class Cell(object):
    def __init__(self):
        self.num = 0
        self.isOpen = False

def newBoard(row, col):
    board = [[Cell() for x in range(row)] for y in range(col)]
    return board

def setMine(board, num):
    i = 0
    while i < num:
        y = randint(0, len(board) - 1)
        x = randint(0, len(board[0]) - 1)
        if board[y][x].num == 0:
            board[y][x].num = -1
            i += 1
    return countMine(board)

def countMine(board):
    for y in range(len(board)):
        if y == 0:
            for x in range(len(board[0])):
                if board[y][x].num != -1:
                    if x == 0:
                        if board[y][x + 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x].num == -1: board[y][x].num += 1
                        if board[y + 1][x + 1].num == -1: board[y][x].num += 1
                    elif x == len(board[0]) - 1:
                        if board[y][x - 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x].num == -1: board[y][x].num += 1
                    else:
                        if board[y][x - 1].num == -1: board[y][x].num += 1
                        if board[y][x + 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x].num == -1: board[y][x].num += 1
                        if board[y + 1][x + 1].num == -1: board[y][x].num += 1
        elif y == len(board) - 1:
            for x in range(len(board[0])):
                if board[y][x].num != -1:
                    if x == 0:
                        if board[y - 1][x].num == -1: board[y][x].num += 1
                        if board[y - 1][x + 1].num == -1: board[y][x].num += 1
                        if board[y][x + 1].num == -1: board[y][x].num += 1
                    elif x == len(board[0]) - 1:
                        if board[y - 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y - 1][x].num == -1: board[y][x].num += 1
                        if board[y][x - 1].num == -1: board[y][x].num += 1
                    else:
                        if board[y - 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y - 1][x].num == -1: board[y][x].num += 1
                        if board[y - 1][x + 1].num == -1: board[y][x].num += 1
                        if board[y][x - 1].num == -1: board[y][x].num += 1
                        if board[y][x + 1].num == -1: board[y][x].num += 1
        else:
            for x in range(len(board[0])):
                if board[y][x].num != -1:
                    if x == 0:
                        if board[y - 1][x].num == -1: board[y][x].num += 1
                        if board[y - 1][x + 1].num == -1: board[y][x].num += 1
                        if board[y][x + 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x].num == -1: board[y][x].num += 1
                        if board[y + 1][x + 1].num == -1: board[y][x].num += 1
                    elif x == len(board[0]) - 1:
                        if board[y - 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y - 1][x].num == -1: board[y][x].num += 1
                        if board[y][x - 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x].num == -1: board[y][x].num += 1
                    else:
                        if board[y - 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y - 1][x].num == -1: board[y][x].num += 1
                        if board[y - 1][x + 1].num == -1: board[y][x].num += 1
                        if board[y][x - 1].num == -1: board[y][x].num += 1
                        if board[y][x + 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x - 1].num == -1: board[y][x].num += 1
                        if board[y + 1][x].num == -1: board[y][x].num += 1
                        if board[y + 1][x + 1].num == -1: board[y][x].num += 1
    return board

def printBoard(board):
    for row in board:
        string = ""
        for col in row:
            if col.num == -1:
                string = string + "x "
            else: 
                string = string + str(col.num) + " "
        print(string)