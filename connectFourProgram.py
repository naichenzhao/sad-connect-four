# Code for the connect 4 game
# ill probably add a GI aspect some time later
# I wanna fucking die

# bloody damn thing works now
# Gosh is it annoying working with Tkinter

'''|--------------------------------------| SHIT LEFT TO DO |--------------------------------------|

TODO: There is this weird bub where the names dont delete each other.
        -Ill figure out what to do later. Im lazy

TODO: probably add an easier way for the users to insert names
        - Maybe make a 'state machine' where each phase is a state and it cycles through

 |-------------------------------------------------------------------------------------------------|'''







''' |--------------------------------------| Imports + Main Setup |--------------------------------------| '''

from tkinter import *
from tkinter import messagebox
import random
import sys
import os
window = Tk()

window.title("Connect Four Game")
window.geometry('700x500')


''' |--------------------------------------| Functions |--------------------------------------| '''

# Adds a chip to a certain column
def addChip( col, colour):
    counter = 0
    for i in table[col-1]:
        if i == " ":
            table[col-1][counter ] = colour
            break
        counter = counter + 1


# Adds a chip co a column and also checks if there is room
def dispPlaceChip(col, player):
    if table[col-1][len(table[0])-1] == " ":
        addChip(col, player)
        return True
    else:
        messagebox.showinfo('Error', "You have placed a chip in an invalid spot")
        return False


# Prints the entire list
def printList():
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][len(table[0])-i-1], end = "  ")
        print()

    for i in colDir:
        print(i, end = "  ")
    print()


# Places a chip. This is not button
def placeChip(location, player):
    location = input("Please indicate which row you would like to place your chip")
    while True:
        if location <= 7:
            addChip(location, player)
            break
        else:
            location = input("Please indicate which row you would like to place your chip")


# Checks if a given person has won the game
def checkConnectFour(value):
    tempCount = 0

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == value:
                for k in range(j,len(table[0])):
                    if table[i][k] == value:
                        tempCount = tempCount + 1
                    else:
                        tempCount = 0
                        break
                    if tempCount >= 4:
                        return True

                tempCount = 0

                for k in range(i, len(table)):
                    if table[k][j] == value:
                        tempCount = tempCount + 1
                    else:
                        tempCount = 0
                        break
                    if tempCount >= 4:
                        return True

                tempCount = 0

                for k in range(len(table)):

                    if i+k >= len(table) or j-k < 0:
                        break
                    if table[i+k][j-k] == value:
                        tempCount = tempCount + 1
                    else:
                        tempCount = 0
                        break
                    if tempCount >= 4:
                        return True

                tempCount = 0

                for k in range(len(table)):

                    if i-k < 0 or j+k >= len(table[0]):
                        break
                    if table[i-k][j+k] == value:
                        tempCount = tempCount + 1
                    else:
                        tempCount = 0
                        break
                    if tempCount >= 4:
                        return True

                tempCount = 0

                for k in range(len(table)):

                    if i-k < 0 or j-k < 0:
                        break
                    if table[i-k][j-k] == value:
                        tempCount = tempCount + 1
                    else:
                        tempCount = 0
                        break
                    if tempCount >= 4:
                        return True

                tempCount = 0

                for k in range(len(table)):

                    if i+k >= len(table) or j+k >= len(table[0]):
                        break
                    if table[i+k][j+k] == value:
                        tempCount = tempCount + 1
                    else:
                        tempCount = 0
                        break
                    if tempCount >= 4:
                        return True

                tempCount = 0

    return False


# Checks if the players are all stupid and the game has somehow ended in a stalemate
def checkStalemate():
    counter = 0
    for i in range(len(table)):
        for j in table[i]:
            if j == " ":
                counter += 1

    if counter == 0:
        return True
    else:
        return False


# Checks which person has won the game
def checkWinner():
    if checkConnectFour(playerDict.get(player1)):
        print("\n", "\n", player1, "has won the game")
    elif checkConnectFour(playerDict.get(player2)):
        print("\n", "\n", player2, "has won the game")


# sets up the GUI game list
def dispArraySetup():
    for i in range(len(table[0])):
        for j in range(len(table)):
            if table[j][len(table[0])-i-1] == "R":
                dTable[j].append( Label(
                    window,
                    text = (table[j][len(table[0])-i-1]) + " ",
                    font = ("Times New Romans",30),
                    fg = "red"))

            elif table[j][len(table[0])-i-1] == "Y":
                dTable[j].append( Label(
                    window,
                    text=(table[j][len(table[0]) - i - 1]) + " ",
                    font=("Times New Romans", 30),
                    fg="orange"))
            else:
                dTable[j].append(Label(
                    window,
                    text=(table[j][len(table[0]) - i - 1]) + " ",
                    font=("Times New Romans", 30),
                    fg="black"))
    for i in range(len(table[0])):
        for j in range(len(table)):
            dTable[j][len(table[0])-i-1].grid(column=j, row=i+3)


# Displays the GUI game list
def dispArray():
    for i in range(len(table[0])):
        for j in range(len(table)):
            if table[j][len(table[0]) - i - 1] == "R":
                dTable[j][len(table[0]) - i - 1] = (Label(
                    window,
                    text=(table[j][len(table[0]) - i - 1]) + " ",
                    font=("Times New Romans", 30),
                    fg="red"))
            elif table[j][len(table[0]) - i - 1] == "Y":
                dTable[j][len(table[0]) - i - 1] = (Label(
                    window,
                    text=(table[j][len(table[0]) - i - 1]) + " ",
                    font=("Times New Romans", 30),
                    fg="orange"))
            else:
                dTable[j][len(table[0]) - i - 1] = (Label(
                    window,
                    text=(table[j][len(table[0]) - i - 1]) + " ",
                    font=("Times New Romans", 30),
                    fg="black"))

    for i in range(len(table[0])):
        for j in range(len(table)):
            dTable[j][len(table[0])-i-1].grid(column=j, row=i+3)


# Sets up the GUI column number display
def dispNumbersSetup():
    for i in range(len(colDir)):
        dColDir.append(Label(window,
                             text = colDir[i] ,
                             font = ("Times New Romans",30),
                             bd = 10))

    for i in range(len(dColDir)):
        dColDir[i].grid(column = i, row = len(table)+5)


# Displays the GUI column number display
def dispNumbers():
    for i in range(len(colDir)):
        dColDir[i] = (Label(window,
                            text = colDir[i] ,
                            font = ("Times New Romans",30),
                            bd = 10))

    for i in range(len(dColDir)):
        dColDir[i].grid(column = i, row = len(table)+5)


#dsplays the title of whose turn it is
def dispPlayerTitle():

    if turnPlayer1 == True:
        title = Label(window,
                      text = "It is currently " + player1 + "\'s turn",
                      font = ("Times New Romans",30),
                      fg="red" )
    elif turnPlayer1 == False:
        title = Label(window,
                      text = "It is currently " + player2 + "\'s turn",
                      font = ("Times New Romans",30),
                      fg="orange" )
    title.grid(
        row=0,
        column = 0,
        columnspan = 7)


# Function to run when a button is clicked
def clicked(number):

    if turnPlayer1 == True:
        if dispPlaceChip(number,playerDict.get(player1)):
            dispArray()
            dispNumbers()
            contiueGame()
            dispPlayerTitle()

    elif turnPlayer1 == False:
        if dispPlaceChip(number,playerDict.get(player2)):
            dispArray()
            dispNumbers()
            contiueGame()
            dispPlayerTitle()


# adds the buttons to teh GUI
def addButtons():
    btn1 = Button(window,
                  text=".",
                  font = ("Times New Romans",30),
                  command=lambda: clicked(1))
    btn1.grid(column=0, row=13)

    btn2 = Button(window,
                  text=".",
                  font = ("Times New Romans",30),
                  command=lambda: clicked(2))
    btn2.grid(column=1, row=13)

    btn3 = Button(window,
                  text=".",
                  font = ("Times New Romans",30),
                  command=lambda: clicked(3))
    btn3.grid(column=2, row=13)

    btn4 = Button(window,
                  text=".",
                  font = ("Times New Romans",30),
                  command=lambda: clicked(4))
    btn4.grid(column=3, row=13)

    btn5 = Button(window,
                  text=".",
                  font = ("Times New Romans",30),
                  command=lambda: clicked(5))
    btn5.grid(column=4, row=13)

    btn6 = Button(window,
                  text=".",
                  font = ("Times New Romans",30),
                  command=lambda: clicked(6))
    btn6.grid(column=5, row=13)

    btn7 = Button(window,
                  text=".",
                  font = ("Times New Romans",30),
                  command=lambda: clicked(7))
    btn7.grid(column=6, row=13)


# Initiates the turns and checks who wins - GUI
def contiueGame():
    global turnPlayer1
    if turnPlayer1 == True:
        if(checkConnectFour(playerDict.get(player1))):
            messagebox.showinfo('The game has ended', 'Congratulations! \n' +  player1 + " has won the game!!")
            exit()
        elif checkStalemate():
            messagebox.showinfo('The game ahs ended', 'Yalls suck at the game. \nIts a stalemate \nBRUH')
            exit()
        else:
            turnPlayer1  = False
    elif turnPlayer1 == False:
        if (checkConnectFour(playerDict.get(player2))):
            messagebox.showinfo('The game ahs ended', 'Congratulations! \n' + player2 + " has won the game!!")
            exit()
        elif checkStalemate():
            messagebox.showinfo('The game ahs ended', 'Yalls suck at the game. \nIts a stalemate \nBRUH')
            exit()
        else:
            turnPlayer1 = True

    printList()



''' |--------------------------------------| Game Setup |--------------------------------------| '''


# Game List

col1 = [" ", " ", " ", " ", " ", " "]
col2 = [" ", " ", " ", " ", " ", " "]
col3 = [" ", " ", " ", " ", " ", " "]
col4 = [" ", " ", " ", " ", " ", " "]
col5 = [" ", " ", " ", " ", " ", " "]
col6 = [" ", " ", " ", " ", " ", " "]
col7 = [" ", " ", " ", " ", " ", " "]
colDir = [1, 2, 3, 4, 5, 6, 7]

table = [col1, col2, col3, col4, col5, col6, col7]

# Display GUI List

dCol1 = []
dCol2 = []
dCol3 = []
dCol4 = []
dCol5 = []
dCol6 = []
dCol7 = []
dColDir = []

dTable = [dCol1, dCol2, dCol3, dCol4, dCol5, dCol6, dCol7]

turnPlayer1 = True


''' |--------------------------------------| Main Gameplay |--------------------------------------| '''

# Get the names
player1 = input("Player 1 please insert your name: ")
player2 = input("Player 2 please insert your name: ")

playerDict = {
    player1:"R",
    player2:"Y"
}


# Print the array first
printList()


# GUI Studd
dispArraySetup()
dispNumbersSetup()
dispPlayerTitle()
addButtons()
window.mainloop()


