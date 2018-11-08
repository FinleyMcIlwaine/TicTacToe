## TicTacToe
## By Finley McIlwaine

from tkinter import *

def clearState():
    global game
    game = gameBoard()
    boardLabel.config(text="X's turn", bg="#808080", fg="white")

def checkState(board, test):
    # board state for winning
    winner = (
        (board[0][0].value==test and board[0][1].value==test and board[0][2].value==test) or
        (board[1][0].value==test and board[1][1].value==test and board[1][2].value==test) or
        (board[2][0].value==test and board[2][1].value==test and board[2][2].value==test) or
        (board[0][0].value==test and board[1][0].value==test and board[2][0].value==test) or
        (board[0][1].value==test and board[1][1].value==test and board[2][1].value==test) or
        (board[0][2].value==test and board[1][2].value==test and board[2][2].value==test) or
        (board[0][0].value==test and board[1][1].value==test and board[2][2].value==test) or
        (board[0][2].value==test and board[1][1].value==test and board[2][0].value==test))

    tie = (game.numTurns==9 and not winner)

    # check states
    if tie:
        game.tie = True
    if winner and game.turn == 1:
        game.xWins = True
    if winner and game.turn == 0:
        game.oWins = True
    
class gameBoard:
    def __init__(self):
        self.board = [
            [boardSpot([0,0]),boardSpot([0,1]),boardSpot([0,2])],
            [boardSpot([1,0]),boardSpot([1,1]),boardSpot([1,2])],
            [boardSpot([2,0]),boardSpot([2,1]),boardSpot([2,2])]
        ]
        self.numTurns  = 0
        self.turn  = 1
        self.allowMove = 0
        self.xWins = False
        self.oWins = False
        self.tie   = False

    def makeMove(self, ind):
        self.numTurns += 1
        self.board[ind[0]][ind[1]].value = self.turn
        checkState(self.board, self.turn)
        if self.turn == 1:
            self.board[ind[0]][ind[1]].btn.config(image=xImg)
            boardLabel.config(text="O's turn")
        if self.turn == 0:
            self.board[ind[0]][ind[1]].btn.config(image=oImg)
            boardLabel.config(text="X's turn")
        self.turn = 1 if self.turn == 0 else 0

        if self.xWins:
            boardLabel.config(text="X wins!!", bg="white", fg="green")
            self.allowMove = 1
        if self.oWins:
            boardLabel.config(text="O wins!!", bg="white", fg="green")
            self.allowMove = 1
        if self.tie:
            boardLabel.config(text="It's a tie!", bg="white", fg="red")
            self.allowMove = 1

class boardSpot:
    def __init__(self, ind):
        # initialize board spot members
        self.value = -1
        self.ind = ind
        self.btn = Button(boardFrame, bg="#333333", image=empty, command=self.clicked)
        self.btn.grid(row=self.ind[0], column=self.ind[1])

    # handles move input
    def clicked(self):
        # check if the spot already has a value
        # and if moves are allowed
        if self.value!=-1 or game.allowMove==1:
            return None
        else:
            game.makeMove(self.ind)

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
game = gameBoard()

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
boardLabel.pack(pady=(30,5))

root.mainloop()