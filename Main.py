import Functions
import ai
import os
from art import *
from termcolor import colored, cprint

def main_menu():
    text=text2art('In', font='block',chr_ignore=True)
    text2=text2art('Row', font='block',chr_ignore=True)
    cprint(text, "cyan", attrs=["bold"], )
    cprint(text2, "cyan", attrs=["bold"])
    cprint("by In 3 Calories\n", "red", attrs=["bold"])
    gameplay = 0
    cprint('(1) Player vs Player\n(2) Player vs AI\n(3) Exit', "yellow", attrs=["bold"])
    menunumber = int(input(" Give me a number: "))
    return menunumber

def pvp():
    name1 = input("Player1's name? ")
    name2 = input("Player2's name? ")
    play = 1
    player=1
    while play!=0:
        board=Functions.start_board()
        os.system('clear')
        Functions.printboard(board)
        game=1
        while game==1:
            if player==1:
                cprint(name1+" turn!", "red", attrs=["bold"])
            else:
                cprint(name2+" turn!", "green", attrs=["bold"])
            coord=Functions.player_move(board)
            if coord==None:
                return None
            board=Functions.move(board,coord,player)
            if player==1:
                player=2
            else:
                player=1
            os.system('clear')
            Functions.printboard(board)
            actual_result=Functions.wincheck(board)
            if actual_result==1:
                cprint(name1+ ' has won!', "red", attrs=["bold"])
                game=0
            if actual_result==2:
                cprint(name2+" has won!" , "green", attrs=["bold"])
                game=0
            if game==1:
                gamedraw=Functions.fullcheck(board)
                if gamedraw==1:
                    cprint("This game is a Draw!", "cyan", attrs=["bold"])
                    game=0
        answer="z"
        while answer!="n":
            answer= input("Do you want to play again? y or n: ")
            if answer=="n":
                play=0
                break
            if answer=="y":
                break

def pvA():
    name1 = input("Player1's name? ")
    play = 1
    player=1
    while play!=0:
        board=Functions.start_board()
        os.system('clear')
        Functions.printboard(board)
        game=1
        while game==1:
            if player==1:
                cprint(name1+" turn!", "red", attrs=["bold"])
                coord=Functions.player_move(board)
                if coord==None:
                    return None
            else:
                coord=ai.ai_move(board)
            board=Functions.move(board,coord,player)
            if player==1:
                player=2
            else:
                player=1
            os.system('clear')
            Functions.printboard(board)
            actual_result=Functions.wincheck(board)
            if actual_result==1:
                cprint(name1+ ' has won!', "red", attrs=["bold"])
                game=0
            if actual_result==2:
                cprint("Computer has won! :(", "yellow", attrs=["bold"])
                game=0
            if game==1:
                gamedraw=Functions.fullcheck(board)
                if gamedraw==1:
                    cprint("This game is a Draw!", "cyan", attrs=["bold"])
                    game=0
        answer = "z"
        while answer != "n":
            answer = input("Do you want to play again? y or n: ")
            if answer == "n":
                play = 0
                break
            if answer == "y":
                break



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


