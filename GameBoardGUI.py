from filePaths import texture
from tkinter import *
import Constants
from Game import *

class GameBoardGUI(Game):

    def __init__(self, master=None, gameType='CvP'):
        super().__init__(gameType)
        self.master = master
        self.loadTextures()
        self.scorePlayer1= Label(master=self.master, bg = Constants.COLOR_BACKGROUND, font = "Helvetica 34 bold")
        self.scorePlayer2 = Label(master=self.master, bg = Constants.COLOR_BACKGROUND, font = "Helvetica 34 bold") 
        
       
    def loadTextures(self):
        self.emptyTileImg = PhotoImage(file=texture.EMPTY_TILE_TEXTURE_PATH)
        self.crossImg = PhotoImage(file=texture.CROSS_TEXTURE_PATH)
        self.circleImg = PhotoImage(file=texture.CIRCLE_TEXTURE_PATH)
        self.gameboardImg = PhotoImage(file=texture.GAMEBOARD_TEXTURE_PATH)
        self.frameImg = PhotoImage(file=texture.GAMEBOARD_FRAME_TEXTURE_PATH)
    
    def run(self, markPlayer1 = 'X'):
        self.updatePlayers(markPlayer1)
        self.buildGameboard()
        self.buildTiles()
        self.buildScore()

        while not self.isGameOver():
            self.master.update_idletasks()
            self.master.update()
            self.computerMoveIfGameIsntOver()
        self.updateScores()

    def buildGameboard(self):
        self.frame = Label(master=self.master, bg=Constants.COLOR_BACKGROUND, image=self.frameImg)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        self.gameBoard = Label(master=self.master, bg="black", image=self.gameboardImg)
        self.gameBoard.grid_anchor('center')
        self.gameBoard.place(relx=0.5, rely=0.5, anchor='center')

    def buildTiles(self):
        w, h = (3,3)
        self.tiles = [[0 for x in range(w)] for y in range(h)] 
        for i in range(w):
            for j in range(h):
                self.tiles[i][j] = Button(master=self.gameBoard, bg="black", activebackground="black", text=' ', borderwidth=0, image=self.emptyTileImg, height=262, width=262)
                self.tiles[i][j]['command'] = lambda x=i, y=j: self.click(x,y)
                self.tiles[i][j].grid(row=i, column=j)
                if i == 1 and j == 1:
                    self.tiles[i][j].grid(padx=7, pady=7)

    def click(self, x, y):
        if self.tiles[x][y]["text"] == ' ':
            self.playerMoveIfGameIsntOver(x, y)

    def playerMoveIfGameIsntOver(self, x, y):
        if self.isGameOver():
            self.disableAllTiles()
        else:
            markToPut = self.getMarkToPut()
            textureToPut = self.getTextureToPut(markToPut)
    
            self.changeTileTexture(self.tiles[x][y], textureToPut, markToPut)
            self.putMarkOnGameboard(x, y, markToPut)
            self.checkForWinner(markToPut)
            self.updateScoreIfIsWinner()
            self.switchCurrentPlayer()
            self.disableTile(self.tiles[x][y])

        if self.isGameOver():
            self.disableAllTiles()

    def disableAllTiles(self):
        w, h = (3, 3)
        for i in range(w):
            for j in range(h):
                self.disableTile(self.tiles[i][j])

    def getTextureToPut(self, mark):
        if mark == 'X':
            return self.crossImg
        if mark == 'O':
            return self.circleImg

    def changeTileTexture(self, tile, texture, mark):
        tile["image"] = texture
        tile["text"] = mark

    def disableTile(self, tile):
        tile['command'] = 0
        tile['relief'] = 'sunken'

    def buildScore(self):
        name1, name2 = self.getPlayerNames()
        score1, score2 = self.getPlayerScores()
        self.scorePlayer1["text"] = f"{name1}: {score1}"
        self.scorePlayer2["text"] = f"{name2}: {score2}"
        self.scorePlayer1.place(relx=0.1, rely=0.1, anchor='w')
        self.scorePlayer2.place(relx=0.9, rely=0.1, anchor='e')

    def computerMoveIfGameIsntOver(self):
        if self.isGameOver():
            self.disableAllTiles()
        else:
            if self.isPlayerVsComputer() and self.isComputerCurrentPlayer():
                move = self.getComputerMove()
                markToPut = self.getMarkToPut()
                textureToPut = self.getTextureToPut(markToPut)
            
                self.changeTileTexture(self.tiles[move[0]][move[1]], textureToPut, markToPut)
                self.putMarkOnGameboard(move[0], move[1], markToPut)
                self.checkForWinner(markToPut)
                self.updateScoreIfIsWinner()
                self.switchCurrentPlayer()
                self.disableTile(self.tiles[move[0]][move[1]])
                
        if self.isGameOver():
            self.disableAllTiles()

    def updateScores(self):
        name1, name2 = self.getPlayerNames()
        score1, score2 = self.getPlayerScores()
        self.scorePlayer1["text"] = f"{name1}: {score1}"
        self.scorePlayer2["text"] = f"{name2}: {score2}"

    def deactivate(self):
        w, h = (3,3)
        for i in range(w):
            for j in range(h):
                self.tiles[i][j].grid_forget()
        
        self.frame.destroy()
        self.gameBoard.destroy()
        self.reset()

if __name__ == "__main__":

    root = Tk()
    root.geometry("1920x1080")
    backgroundTexture = PhotoImage(file=texture.BACKGROUND_TEXTURE_PATH)
    background = Label(master=root, image=backgroundTexture).place(x=0,y=0)
    frameTexture = PhotoImage(file=texture.GAMEBOARD_FRAME_TEXTURE_PATH)
    frame = Label(master=root, bg=Constants.COLOR_BACKGROUND, image=frameTexture).place(relx=0.5, rely=0.5, anchor='center')
    gameBoard = GameBoardGUI(root)
    gameBoard.run()
   