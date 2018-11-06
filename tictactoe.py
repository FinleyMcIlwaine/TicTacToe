## TicTacToe
## By Finley McIlwaine

from tkinter import *

# global turn variable
# 1 -> X's turn
# 0 -> O's turn
turn = 1
# global allow move variable
# 1 -> not allowed
# 0 -> allowed
allowMove = 0
# global # of turns variable
# -> tells number of turns
#    made during round
numTurns = 0

def clearState():
    global turn
    global board
    global allowMove
    global numTurns
    # reset the turn label
    boardLabel.config(text="X's turn!", font=("Bookman", 15), bg="#808080", fg="white")
    # reset the turn variable
    turn = 1
    # reset the allow move bool
    allowMove = 0
    # reset the number of turns for the round
    numTurns = 0

    # reinitialize the board
    board = [
        boardSpot([0,0]),boardSpot([0,1]),boardSpot([0,2]),
        boardSpot([1,0]),boardSpot([1,1]),boardSpot([1,2]),
        boardSpot([2,0]),boardSpot([2,1]),boardSpot([2,2]),
    ]

def checkState(board):
    global allowMove
    global numTurns
    # board states for X winning
    test=1
    Xwinner = (
        (board[0].value==test and board[1].value==test and board[2].value==test) or
        (board[3].value==test and board[4].value==test and board[5].value==test) or
        (board[6].value==test and board[7].value==test and board[8].value==test) or
        (board[0].value==test and board[3].value==test and board[6].value==test) or
        (board[1].value==test and board[4].value==test and board[7].value==test) or
        (board[2].value==test and board[5].value==test and board[8].value==test) or
        (board[0].value==test and board[4].value==test and board[8].value==test) or
        (board[2].value==test and board[4].value==test and board[6].value==test))

    # board states for O winning
    test=0
    Owinner = (
        (board[0].value==test and board[1].value==test and board[2].value==test) or
        (board[3].value==test and board[4].value==test and board[5].value==test) or
        (board[6].value==test and board[7].value==test and board[8].value==test) or
        (board[0].value==test and board[3].value==test and board[6].value==test) or
        (board[1].value==test and board[4].value==test and board[7].value==test) or
        (board[2].value==test and board[5].value==test and board[8].value==test) or
        (board[0].value==test and board[4].value==test and board[8].value==test) or
        (board[2].value==test and board[4].value==test and board[6].value==test))

    # board state for a tie
    tie = (numTurns==9 and not (Owinner or Xwinner))

    # check states
    if tie:
        boardLabel.config(text="It's a tie!", bg="white", fg="red")
        allowMove = 1
    if Xwinner:
        boardLabel.config(text="X wins!!", bg="white", fg="green")
        allowMove = 1
    if Owinner:
        boardLabel.config(text="O wins!!", bg="white", fg="green")
        allowMove = 1
    

class boardSpot:
    def __init__(self, ind):
        # initialize board spot members
        self.value = -1
        self.ind = ind
        self.btn = Button(boardFrame, bg="#333333", image=empty, command=self.clicked)
        self.btn.grid(row=self.ind[0], column=self.ind[1])

    # handles move input
    def clicked(self):
        global allowMove

        # check if the spot already has a value
        # and if moves are allowed
        if self.value!=-1 or allowMove==1:
            return None
        else:
            self.makeMove()

    # exectutes a move
    def makeMove(self):
        global turn
        global numTurns

        # set the value of the board spot
        self.value = turn
        # check whose turn it was and set
        # board state appropriately
        if turn==1:
            self.btn.config(image=xImg)
            turn = 0
            boardLabel.config(text="O's turn!")
        else:
            self.btn.config(image=oImg)
            turn = 1
            boardLabel.config(text="X's turn!")
        
        # increment number of turns
        numTurns += 1
        # check for win state
        checkState(board)

# set up window
root = Tk()
root.title("TicTacToe!")
root.iconbitmap("./pngs/favicon.ico")
root.geometry('500x500')
root.resizable(0, 0)
root.configure(background='#808080')

# define images
xImg = PhotoImage(file="./pngs/X.png")
oImg = PhotoImage(file="./pngs/O.png")
empty= PhotoImage(file="./pngs/empty.png")

# define board object
boardFrame = Frame(root)
boardFrame.pack(side='bottom', pady=(0,30))
board = [
    boardSpot([0,0]),boardSpot([0,1]),boardSpot([0,2]),
    boardSpot([1,0]),boardSpot([1,1]),boardSpot([1,2]),
    boardSpot([2,0]),boardSpot([2,1]),boardSpot([2,2]),
]

# const header labels
titleLabel = Label(root, text="TicTacToe!", font=("Impact",20))
titleLabel.pack(fill=X)
nameLabel = Label(root, text="By Finley McIlwaine", font=("Bookman",8))
nameLabel.pack(fill=X)

# reset button
resetBtn = Button(root, bg="#808080", fg="white", text="Reset", font=("Bookman",10), height=1, width=15, command=clearState)
resetBtn.pack(pady=(5,0))

# label object to tell turn/state
boardLabel = Label(root, text="X's turn!", font=("Bookman", 15), bg="#808080", fg="white")
boardLabel.pack(pady=(30,0))

root.mainloop()