import Functions
import random

def ai_move(board):
    board_size = len(board)
    if board_size <= 4:
        return ai_think_three(board)
    elif board_size < 8 and board_size > 4:
        return ai_think_four(board)
    elif board_size > 7:
        return ai_think_five(board)

def ai_move_check(board, row, col):
    matrix_size = len(board)
    if matrix_size < 5:
        checklenght = 3
    elif matrix_size > 4 and matrix_size < 8:
        checklenght = 4
    elif matrix_size > 7:
        checklenght = 5
    raw_board_line = []
    if matrix_size < 5:
        checking_rows = [[[-2, -2], [-1, -1], [0, 0]], [[-1, -1], [0, 0], [1, 1]], [[0, 0], [1, 1], [2, 2]],
                         [[0, -2], [0, -1], [0, 0]], [[0, -1], [0, 0], [0, 1]], [[0, 0], [0, 1], [0, 2]],
                         [[2, -2], [1, -1], [0, 0]], [[1, -1], [0, 0], [-1, 1]], [[0, 0], [-1, 1], [-2, 2]],
                         [[-2, 0], [-1, 0], [0, 0]], [[-1, 0], [0, 0], [1, 0]], [[0, 0], [1, 0], [2, 0]]]
        for z in range(len(checking_rows)):
            raw_board_line.append([])
        for i in range(len(checking_rows)):
            for y in range(3):
                raw_board_line[i].append([row + checking_rows[i][y][0], col + checking_rows[i][y][1]])

    elif matrix_size > 4 and matrix_size < 8:
        checking_rows = [[[-3, -3], [-2, -2], [-1, -1], [0, 0]], [[-2, -2], [-1, -1], [0, 0], [1, 1]], [[-1, -1], [0, 0], [1, 1], [2, 2]], [[0, 0], [1, 1], [2, 2], [3, 3]],
                         [[0, -3], [0, -2], [0, -1], [0, 0]], [[0, -2], [0, -1], [0, 0], [0, 1]], [[0, -1], [0, 0], [0, 1], [0, 2]], [[0, 0], [0, 1], [0, 2], [0, 3]],
                         [[-3, 3], [-2, 2], [-1, 1], [0, 0]], [[-2, 2], [-1, 1], [0, 0], [1, -1]], [[-1, 1], [0, 0], [1, -1], [2, -2]], [[0, 0], [1, -1], [2, -2], [3, -3]],
                         [[-3, 0], [-2, 0], [-1, 0], [0, 0]], [[-2, 0], [-1, 0], [0, 0], [1, 0]], [[-1, 0], [0, 0], [1, 0], [2, 0]], [[0, 0], [1, 0], [2, 0], [3, 0]]]
        for z in range(len(checking_rows)):
            raw_board_line.append([])
        for i in range(len(checking_rows)):
            for y in range(4):
                raw_board_line[i].append([row + checking_rows[i][y][0], col + checking_rows[i][y][1]])

    elif matrix_size > 7:
        checking_rows = [[[-4, -4], [-3, -3], [-2, -2], [-1, -1], [0, 0]], [[-3, -3], [-2, -2], [-1, -1], [0, 0], [1, 1]], [[-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2]], [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3]], [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],
                         [[0, -4], [0, -3], [0, -2], [0, -1], [0, 0]], [[0, -3], [0, -2], [0, -1], [0, 0], [0, 1]], [[0, -2], [0, -1], [0, 0], [0, 1], [0, 2]], [[0, -1], [0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
                         [[-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0]], [[-3, 3], [-2, 2], [-1, 1], [0, 0], [1, -1]], [[-2, 2], [-1, 1], [0, 0], [1, -1], [2, -2]], [[-1, 1], [0, 0], [1, -1], [2, -2], [3, -3]], [[0, 0], [1, -1], [2, -2], [3, -3], [4, -4]],
                         [[-4, 0], [-3, 0], [-2, 0], [-1, 0], [0, 0]], [[-3, 0], [-2, 0], [-1, 0], [0, 0], [1, 0]], [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]], [[-1, 0], [0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]]
        for z in range(len(checking_rows)):
            raw_board_line.append([])
        for i in range(len(checking_rows)):
            for y in range(5):
                raw_board_line[i].append([row + checking_rows[i][y][0], col + checking_rows[i][y][1]])

    board_line = Functions.board_line_add(Functions.negative_check(raw_board_line), board)
    for m in range(len(board_line)):
        if len(board_line[m]) != checklenght:
            board_line[m] = []
    return board_line

def ai_think_three(board):
    hierarhic = [[], [], [], [], [], []]
    steps = {5: [[2, 2, 0], [2, 0, 2], [0, 2, 2]],
             4: [[1, 1, 0], [1, 0, 1], [0, 1, 1]],
             3: [[2, 0, 0], [0, 2, 0], [0, 0, 2]],
             2: [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
             1: [[]],
             0: [0, 0, 0]}
    for i in range(len(board)):
        for y in range(len(board[i])):
            if board[i][y] == 0:
                check = ai_move_check(board, i, y)
                check = filter(None, check)
                for z in check:
                    for key, value in steps.items():
                        if z in value:
                            coord = [i, y]
                            if coord not in hierarhic[key]:
                                hierarhic[key].append(coord)
                        elif z == value:
                            coord = [i, y]
                            if coord not in hierarhic[0]:
                                hierarhic[0].append(coord)
                        else:
                            coord = [i, y]
                            if coord not in hierarhic[1]:
                                hierarhic[1].append(coord)
            else:
                continue
    hierarhic.reverse()
    for x in range(len(hierarhic)):
        if hierarhic[x] != []:
            ind = random.randrange(0, len(hierarhic[x]))
            return hierarhic[x][ind]

def ai_think_four(board):
    hierarhic = [[], [], [], [], [], [], [], []]
    steps = {7: [[2, 2, 2, 0], [2, 2, 0, 2], [2, 0, 2, 2], [0, 2, 2, 2]],
             6: [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]],
             5: [[0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]],
             4: [[0, 2, 2, 0], [0, 2, 0, 1], [2, 0, 2, 0]],
             3: [[0, 0, 0, 2], [0, 0, 2, 0], [0, 2, 0, 0], [2, 0, 0, 0]],
             2: [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]],
             1: [[]],
             0: [0, 0, 0, 0]}

    for i in range(len(board)):
        for y in range(len(board[i])):
            if board[i][y] == 0:
                check = ai_move_check(board, i, y)
                check = filter(None, check)
                for z in check:
                    for key, value in steps.items():
                        if z in value:
                            coord = [i, y]
                            if coord not in hierarhic[key]:
                                hierarhic[key].append(coord)
                        elif z == value:
                            coord = [i, y]
                            if coord not in hierarhic[0]:
                                hierarhic[0].append(coord)
                        else:
                            coord = [i, y]
                            if coord not in hierarhic[1]:
                                hierarhic[1].append(coord)
            else:
                continue
    hierarhic.reverse()
    for x in range(len(hierarhic)):
        if hierarhic[x] != []:
            ind = random.randrange(0, len(hierarhic[x]))
            return hierarhic[x][ind]

def ai_think_five(board):
    hierarhic = [[], [], [], [], [], [], [], []]
    steps = {7: [[0, 2, 2, 2, 2], [2, 0, 2, 2, 2], [2, 2, 0, 2, 2], [2, 2, 2, 0, 2], [2, 2, 2, 2, 0]],
             6: [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]],
             5: [[0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 1, 0, 1]],
             4: [[0, 2, 2, 2, 0], [2, 0, 2, 2, 0], [0, 2, 2, 0, 2]],
             3: [[0, 2, 0, 2, 0], [2, 0, 2, 0, 0], [2, 2, 0, 0, 0], [0, 2, 2, 0, 0], [0, 2, 0, 0, 2], [2, 0, 0, 2, 0], [2, 0, 0, 0, 2]],
             2: [[0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1]],
             1: [],
             0: [0, 0, 0, 0, 0]}
    for i in range(len(board)):
        for y in range(len(board[i])):
            if board[i][y] == 0:
                check = ai_move_check(board, i, y)
                check = filter(None, check)
                for z in check:
                    for key, value in steps.items():
                        if z in value:
                            coord = [i, y]
                            if coord not in hierarhic[key]:
                                hierarhic[key].append(coord)
                        elif z == value:
                            coord = [i, y]
                            if coord not in hierarhic[0]:
                                hierarhic[0].append(coord)
                        else:
                            coord = [i, y]
                            if coord not in hierarhic[1]:
                                hierarhic[1].append(coord)
            else:
                continue
    hierarhic.reverse()
    for x in range(len(hierarhic)):
        if hierarhic[x] != []:
            ind = random.randrange(0, len(hierarhic[x]))
            return hierarhic[x][ind]

