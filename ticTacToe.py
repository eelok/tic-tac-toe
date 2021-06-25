#!/usr/bin/python3

field = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

player = "X"
run = True

def print_field(field):
    for row in range(len(field)):
        for column in range(len(field)):
            print(field[row][column], end=' ')
        print()    

def user_input(pl, playIsRunning):
    while playIsRunning: 
        definePlayer(pl)
        userInputStrint = input("Insert field.\nExample: row,column\nExample: 0,1\n")
        inputArray = userInputStrint.split(",")
        row = int(inputArray[0])
        column = int(inputArray[1])
        if(field[row][column] == "*"):
            field[row][column] = pl
            print_field(field)
            playIsRunning = findWinner(field, pl)
            pl = switchPlayer(pl)
        else:
            print("The field is taken")    
        

def definePlayer(aPlayer):
    if aPlayer == "X":
        print("FIRST player:", aPlayer)
    else:
        print("SECOND player:", aPlayer)

def switchPlayer(aPlayer):
    if aPlayer == "X":
        return "O"
    else:
        return "X"    


def wonMessage(pl):
    print ("GAME OVER\nPlayer", pl, "won")
    return False

def findWinner(field, pl):
    if field[0][0] == field[0][1] == field[0][2] == pl:
        return wonMessage(pl)
    elif field[1][0] == field[1][1] == field[1][2] == pl:
        return wonMessage(pl)
    elif field[2][0] == field[2][1] == field[2][2] == pl:
        return wonMessage(pl)
    elif field[0][0] == field[0][1] == field[0][2] == pl:
        return wonMessage(pl)
    elif field[0][1] == field[1][1] == field[2][1] == pl:
        return wonMessage(pl)
    elif field[0][2] == field[1][2] == field[2][2] == pl:
        return wonMessage(pl)       
    elif field[0][0] == field[1][1] == field[2][2] == pl:
        return wonMessage(pl)
    elif field[0][2] == field[1][1] == field[2][0] == pl:
        return wonMessage(pl)  
    else:
        return True    


print_field(field)
user_input(player, run)
