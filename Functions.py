import copy
from termcolor import *

def init_board(matrix_size):
    matrix = []
    for i in range(matrix_size):
        row = []
        matrix.append(row)
        for y in range(matrix_size):
            row.append(0)
    return matrix

def get_move(old_board, matrix_size):
    board = old_board
    raw_row_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    raw_col_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    row_list = raw_row_list[0:matrix_size]
    col_list = raw_col_list[0:matrix_size]
    row = None
    col = None
    c = 0
    while c == 0:
        while not row in row_list:
            try:
                row = input("Give me the row's letter: ").upper()
            except:
                print("Please enter a valid letter!")
                continue
        while not col in col_list:
            try:
                col = int(input("Give me the column's number: "))
            except:
                print("Please enter a valid number!")
                continue
        if board[row_list.index(row)][col_list.index(col)] != 0:
            row = None
            col = None
            print("Someone already put there!")
            continue
        else:
            c = 1
    coord = (row_list.index(row), col_list.index(col))
    return coord

def mark(move, main_board, player):
    board = main_board
    row = move[0]
    col = move[1]
    board[row][col] = player
    return board

def print_board(x, matrix_size):
    board = copy.deepcopy(x)
    for i in range(len(x)):
        for y in range(len(x[i])):
            if x[i][y] == 0:
                board[i][y] = '.'
            elif x[i][y] == 1:
                board[i][y] = colored('X', 'red', attrs=['bold'])
            elif x[i][y] == 2:
                board[i][y] = colored('O', 'green', attrs=['bold'])
    raw_col = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    colum = raw_col[0:matrix_size]
    colum = '   '.join(colum)
    raw_row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    row = raw_row[0:matrix_size]
    print('    ', colum)
    count = 0
    while count < matrix_size:
        row_board = board[count]
        row_board = ' | '.join(row_board)
        print(row[count], '  ', row_board)
        count += 1

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

def has_won(board, matrix_size):
    if matrix_size < 5:
        player1_win = [1, 1, 1]
        player2_win = [2, 2, 2]
        for i in range(len(board)):
            for y in range(len(board[i])):
                check = win_check_list(board, matrix_size, i, y)
                if player1_win in check:
                    return True, 1
                elif player2_win in check:
                    return True, 2
                else:
                    continue
        return False, 0

    elif matrix_size > 4 and matrix_size < 8:
        player1_win = [1, 1, 1, 1]
        player2_win = [2, 2, 2, 2]
        for i in range(len(board)):
            for y in range(len(board[i])):
                if player1_win in win_check_list(board, matrix_size, i, y):
                    return True, 1
                elif player2_win in win_check_list(board, matrix_size, i, y):
                    return True, 2
                else:
                    continue
        return False, 0

    elif matrix_size > 7:
        player1_win = [1, 1, 1, 1, 1]
        player2_win = [2, 2, 2, 2, 2]
        for i in range(len(board)):
            for y in range(len(board[i])):
                if player1_win in win_check_list(board, matrix_size, i, y):
                    return True, 1
                elif player2_win in win_check_list(board, matrix_size, i, y):
                    return True, 2
                else:
                    continue
        return False, 0


def is_full(board):
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
        
        

        