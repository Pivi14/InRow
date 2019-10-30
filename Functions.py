import copy
from art import *
from termcolor import colored, cprint



def start_board():
    matrix=[]
    size=1
    while size<3 or size>10:
        size=int(input("The size of the board: "))
    for i in range(size):
        row=[]
        matrix.append(row)
        for y in range(size):
            row.append(0)
    return matrix



def player_move(matrix):
    max_lenght=len(matrix)
    abcs_raw=["A","B","C","D","E","F","G","H","I","J"]
    abcs=abcs_raw[0:max_lenght]
    valid_coordinate=False
    while valid_coordinate==False:
        row=None
        while row not in abcs:
            row=input("Give a row: ").upper()
            if row=="QUIT":
                return None
            if row not in abcs:
                cprint("Not valid row!","yellow", attrs=["bold"])
        row=abcs.index(row)
        col=input("Give a column: ")
        try:
            row=int(row)
            col=int(col)
        except:
            continue
        if isinstance(row, int) and isinstance(col, int) and row<=max_lenght and row>=0 and col<=max_lenght and col>0:
            if matrix[row][col-1]==0:
                valid_coordinate=True
        else:
            print("Wrong input, try again!")
    return row,col-1



def move(matrix,coord,player):
    row=coord[0]
    colum=coord[1]
    if player==1:
        matrix[row][colum]=1
    if player==2:
        matrix[row][colum]=2
    return matrix



def printboard(n):
    board = copy.deepcopy(n)
    abcs=["A","B","C","D","E","F","G","H","I","J"]
    for i in range(len(n)):
        for y in range(len(n[i])):
            if n[i][y] == 0:
                board[i][y] = '.'
            elif n[i][y] == 1:
                board[i][y] = colored('X', 'red', attrs=['bold'])
            elif n[i][y] == 2:
                board[i][y] = colored('O', 'green', attrs=['bold'])
    maxlistsizes=["1","2","3","4","5","6","7","8","9","10"]
    print(" "*5 + " | ".join(maxlistsizes[0:len(board)]))
    print("\n")
    for row in range(len(n)):
        print((abcs[row]),"   "+" | ".join(board[row])+'\n')


def negative_check(raw_board_line):
    for i in range(len(raw_board_line)):
        for y in range(len(raw_board_line[i])):
            if raw_board_line[i][y][0] < 0 or raw_board_line[i][y][1] < 0:
                raw_board_line[i][y] = []
    return raw_board_line

def board_line_add(raw_board_line, board):
    new_board_line = []
    for i in range(len(raw_board_line)):
        for y in range(len(raw_board_line[i])):
            if [] in raw_board_line[i]:
                raw_board_line[i][y] = []
    for w in range(len(raw_board_line)):
        new_board_line.append([])
        for z in range(len(raw_board_line[w])):
            if raw_board_line[w][z] != []:
                try:
                    new_board_line[w].append(board[raw_board_line[w][z][0]][raw_board_line[w][z][1]])
                except:
                    continue
            else:
                continue
    return new_board_line

def win_check_list(board, matrix_size, row, col):
    index_change = [[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
                    [[0, 0], [-1, 1], [-2, 2], [-3, 3], [-4, 4]],
                    [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],
                    [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]]
    raw_board_line = [[], [], [], []]
    if matrix_size < 5:
        for i in range(4):
            for y in range(3):
                raw_board_line[i].append([row + index_change[i][y][0], col + index_change[i][y][1]])
    elif matrix_size > 4 and matrix_size < 8:
        for i in range(4):
            for y in range(4):
                raw_board_line[i].append([row + index_change[i][y][0], col + index_change[i][y][1]])
    elif matrix_size > 7:
        for i in range(4):
            for y in range(5):
                raw_board_line[i].append([row + index_change[i][y][0], col + index_change[i][y][1]])
    board_line = board_line_add(negative_check(raw_board_line), board)
    return board_line

def wincheck(board):
    matrix_size = len(board)
    if matrix_size < 5:
        player1_win = [1, 1, 1]
        player2_win = [2, 2, 2]
        for i in range(len(board)):
            for y in range(len(board[i])):
                check = win_check_list(board, matrix_size, i, y)
                if player1_win in check:
                    return 1
                elif player2_win in check:
                    return 2
                else:
                    continue
        return 0

    elif matrix_size > 4 and matrix_size < 8:
        player1_win = [1, 1, 1, 1]
        player2_win = [2, 2, 2, 2]
        for i in range(len(board)):
            for y in range(len(board[i])):
                if player1_win in win_check_list(board, matrix_size, i, y):
                    return 1
                elif player2_win in win_check_list(board, matrix_size, i, y):
                    return 2
                else:
                    continue
        return 0

    elif matrix_size > 7:
        player1_win = [1, 1, 1, 1, 1]
        player2_win = [2, 2, 2, 2, 2]
        for i in range(len(board)):
            for y in range(len(board[i])):
                if player1_win in win_check_list(board, matrix_size, i, y):
                    return 1
                elif player2_win in win_check_list(board, matrix_size, i, y):
                    return 2
                else:
                    continue
        return 0


def fullcheck(board):
    fullboard = board
    board_size = len(board)
    check = 0
    for i in fullboard:
        if 0 not in i:
            check += 1
        else:
            continue
    if check == board_size:
        return True
    else:
        return False