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
    valid_coordinate=False
    max_lenght=len(matrix)
    while valid_coordinate==False:
        row=int(input("Give a row: "))
        col=int(input("Give a column: "))
        if row<=max_lenght and row>0 and col<=max_lenght and col>0:
            if matrix[row-1][col-1]==0:
                valid_coordinate=True
        else:
            print("Wrong input, try again!")
    return row-1,col-1




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
        for i in range(len(n)):
                for y in range(len(n[i])):
                        if n[i][y] == 0:
                                board[i][y] = '.'
                        elif n[i][y] == 1:
                                board[i][y] = colored('X', 'red', attrs=['bold'])
                        elif n[i][y] == 2:
                                board[i][y] = colored('O', 'green', attrs=['bold'])
        maxlistsizes=["1","2","3","4","5","6","7","8","9","10"]
        print(" "*5 + "   ".join(maxlistsizes[0:len(board)]))
        for row in range(len(n)):
                print((row+1),"   "+" | ".join(board[row])+'\n')
