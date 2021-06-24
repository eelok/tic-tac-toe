#!/usr/bin/python3

field = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

counter = 0

playerSymbol = ["X","O"]

def print_field(field):
    for row in range(len(field)):
        for column in range(len(field)):
            print(field[row][column], end=' ')
        print()    

def user_input(playerSymbol, counter):
    print("c: ", counter)
    if(counter == 0):
        print("FIRST player: X")
    else:
        print("SECOND player: O")
    userInputStrint = input("Insert field.\nExample: row,column\nExample: 0,1\n")
    inputArray = userInputStrint.split(",")
    row = int(inputArray[0])
    column = int(inputArray[1])
    if(field[row][column] == "*"):
        field[row][column] = playerSymbol[c]
        print_field(field)
    else:
        print("The field is taken")    
    return switchPlayer(counter)


def switchPlayer(c):
    if c > 0:
        return 0
    else:
        return 1      

print_field(field)
while True: 
    counter = user_input(playerSymbol, counter)
