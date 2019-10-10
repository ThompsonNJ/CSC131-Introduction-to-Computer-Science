#==========================================================================
# PROGRAM PURPOSE:... Ch5 D3
# AUTHOR:............ Thompson, Nick; Ingram, Andrew
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... We pair programmed over Skype via Screen Share
# WORK TIME(h:mm):... 7:10
#==========================================================================
def printnumBrd():
    print(ttt[0], ttt[1], ttt[2])
    print(ttt[3], ttt[4], ttt[5])
    print(ttt[6], ttt[7], ttt[8])


def printgameBrd():
    print()
    print("Current Board:")
    print(gamettt[0], gamettt[1], gamettt[2])
    print(gamettt[3], gamettt[4], gamettt[5])
    print(gamettt[6], gamettt[7], gamettt[8])
    print()

def endgame():
    if gamettt[0] == gamettt[1] == gamettt[2] == "X" or gamettt[0] == gamettt[1] == gamettt[2] == "O":
        return True
    elif gamettt[3] == gamettt[4] == gamettt[5] == "X" or gamettt[3] == gamettt[4] == gamettt[5] == "O":
        return  True   
    elif gamettt[6] == gamettt[7] == gamettt[8] == "X" or gamettt[6] == gamettt[7] == gamettt[8] == "O":
        return  True 
    elif gamettt[0] == gamettt[3] == gamettt[6] == "X" or gamettt[0] == gamettt[3] == gamettt[6] == "O":
        return True   
    elif gamettt[1] == gamettt[4] == gamettt[7] == "X" or gamettt[1] == gamettt[4] == gamettt[7] == "O":
        return True   
    elif gamettt[2] == gamettt[5] == gamettt[8] == "X" or gamettt[2] == gamettt[5] == gamettt[8] == "O":
        return  True   
    elif gamettt[0] == gamettt[4] == gamettt[8] == "X" or gamettt[0] == gamettt[4] == gamettt[8] == "O":
        return  True   
    elif gamettt[2] == gamettt[4] == gamettt[6] == "X" or gamettt[2] == gamettt[4] == gamettt[6] == "O":
        return True   
    else:
        return False


def validmove():
    if pInput >= 0 and pInput <= 8 and not gamettt[pInput].count('X') and not gamettt[pInput].count('O'):
        
        return True
    else:
        print("Invalid Entry")
        return False
    
step = 0
turn = 1
ttt = [0, 1, 2, 3, 4, 5, 6, 7, 8]
gamettt = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
gameover = endgame()
print("Welcome to the game of tic-tac-toe.\n\
Player X will go first followed by Player O.\n\
")
 
print("When it is your turn, pick a number on the board.\n\
You must select a space on the board that has not yet been selected.\n\
After selecting a number on the board, hit enter to end your turn.\n\
")


print("The goal of the game is to get three of your symbols in a row.\n\
GOODLUCK!!!!\n\
")

printnumBrd()
print()


while True:
    try:
        while step < 9:
            if gameover == True:
                if turn == 1:
                    print("Congradulations Player O!")
                if turn == 2:                          
                    print("Congradulations Player X!")
                break

            else:
                pInput = int(input("Pick a number on the board it will be replaced by your symbol: "))      
                if turn == 1 and validmove():
                    print()
                    printnumBrd()
                    gamettt[pInput] = 'X'
                    printgameBrd()
                    turn = 2
                    step += 1
                    gameover = endgame()
                else:
                    if turn == 2 and validmove():
                        printnumBrd()
                        gamettt[pInput] = 'O'
                        printgameBrd()
                        turn = 1
                        step += 1
                        gameover = endgame()
        else:
            print("The game is a tie!")
            break

    except ValueError:
        print()
        print("Sorry! Please enter a number that appears on the board!")
        print()
    else:
        break



