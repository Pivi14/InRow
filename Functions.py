import copy
from art import *
from termcolor import colored, cprint















































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
