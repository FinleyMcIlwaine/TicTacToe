from tkinter import *

# global turn variable
# 1 -> X's turn
# 0 -> O's turn
turn = 1

def checkState(board):
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
    if Xwinner:
        boardLabel.config(text="X wins!!", bg="white", fg="red")
    if Owinner:
        boardLabel.config(text="O wins!!", bg="white", fg="red")

class boardSpot:
    def __init__(self, ind):
        self.value = -1
        self.ind = ind
        self.btn = Button(boardFrame, bg="#333333", image=empty, command=self.clicked)
        self.btn.grid(row=self.ind[0], column=self.ind[1])

    # handles move input
    def clicked(self):
        if self.value!=-1:
            return None
        else:
            self.makeMove()

    # exectutes a move
    def makeMove(self):
        global turn
        self.value = turn
        if turn==1:
            self.btn.config(image=xImg)
            turn = 0
            boardLabel.config(text="O's turn!")
        else:
            self.btn.config(image=oImg)
            turn = 1
            boardLabel.config(text="X's turn!")
        # check for win state
        checkState(board)

# set up window
root = Tk()
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

# const header label
headLabel = Label(root, text="TicTacToe!", font=("Impact",20))
headLabel.pack(side='top', pady=(10,0))

# label object to tell turn/state
boardLabel = Label(root, text="X's turn!", font=("Bookman", 15), bg="#808080", fg="white")
boardLabel.pack(side='top', pady=(50,0))

root.mainloop()