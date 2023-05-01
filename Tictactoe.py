# Prolog
# Author: Darling Ngoh
'''
 Purpose:
 calculating the winner of a tic-tac-toe game
'''

#initializing variables

def tic_tac_toe():
    #printing out instrusting for user
    print ("Please input 3 combineof 'X', 'O', or 'E' as XOE, XXE and so on")

    #getting user values of x, o, or e for 3 rows
    row1 = input("ROW0: ").upper()
    row2 = input("ROW1: ").upper()
    row3 = input("ROW2: ").upper()

    # set orginial bolean values for horizontal, verticle and diagonal to be False
    horizontal = False
    verticle = False
    diagonal = False

    #first check if horizontal xxx or ooo, then verticle, then diagonal
    if row1[0]==row1[1]==row1[2]=='X' or row2[0]==row2[1]==row2[2]=='X' or row3[0]==row3[1]==row3[2]=='X':
        horizontal = True
        print("X is GOOD in horizontal")
    elif row1[0]==row1[1]==row1[2]=='O' or row2[0]==row2[1]==row2[2]=='O' or row3[0]==row3[1]==row3[2]=='O':
        horizontal = True
        print("O is GOOD in horizontal")
    elif row1[0]==row2[0]==row3[0]=='X' or row1[1]==row2[1]==row3[1]=='X'or row1[2]==row2[2]==row3[2]=='X':
        verticle = True
        print("X is GOOD in verticle")
    elif row1[0]==row2[0]==row3[0]=='O' or row1[1]==row2[1]==row3[1]=='O'or row1[2]==row2[2]==row3[2]=='O':
        verticle = True
        print("O is GOOD in verticle")
    elif row1[0]==row2[1]==row3[2]=='X' or row1[2]==row2[1]==row3[0]=='X':
        diagonal = True
        print("X is GOOD in diagonal")
    elif row1[0]==row2[1]==row3[2]=='O' or row1[2]==row2[1]==row3[0]=='O':
        diagonal = True
        print("O is GOOD in diagonal")
    else:
        print("This is a tie")

tic_tac_toe()
