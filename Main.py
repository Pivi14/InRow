import Functions
import os
from art import *
from termcolor import colored, cprint

def main_menu():
    text=text2art('In', font='broadway',chr_ignore=True)
    text2=text2art('Row', font='broadway',chr_ignore=True)
    cprint(text, "yellow", attrs=["bold"], )
    cprint(text2, "white", attrs=["bold"])
    cprint("by In 3 Calories\n", "cyan", attrs=["bold"])
    gameplay = 0
    print(' (1) Player vs Player\n', '(2) Player vs AI\n', '(3) Exit')
    menunumber = int(input())
    return menunumber

def pvp():
    Functions.startboard()
    while Functions.resultprint!=1:
        Functions.player_move()
        Functions.move()
        Functions.printboard()
        Functions.wincheck()
        Functions.fullcheck()
        Functions.resultprint()


def PvP():
    name1 = input("Player1's name? ")
    name2 = input("Player2's name? ")
    play = 1
    player=1
    while play!=0:
        board=Functions.startboard()
        game=1
        while game==1:
            if player==1:
                print(name1+" turn!")
            else:
                print(name2+" turn!")
            coord=Functions.player_move(board)
            board=Functions.move(coord,board,player)
            if player==1:
                player=2
            else:
                player=1
            Functions.printboard(board)
            actual_result=Functions.wincheck(board)
            if actual_result==1:
                print(name1+ ' has won!')
                game=0
            if actual_result==2:
                print(name2+" has won!")
                game=0
            gamedraw=Functions.fullcheck(board)
            if gamedraw==1:
                print("This game is a Draw!")
                game=0
            replay=input("Do you want to play again?: ")
            if replay=="n":
                play=0
    return None
    
           

os.system('clear')
prog = 1
while prog == 1:
    os.system('clear')
    game = main_menu()
    if game == 1:
        pvp()
    elif game == 2:
        pvA()
    elif game == 3:
        prog = 0
os.system('clear')
byetext=text2art("Good Bye", font='broadway', chr_ignore=True)
cprint(byetext, 'yellow', attrs=['bold'])