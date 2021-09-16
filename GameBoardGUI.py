from filePaths import texture
from tkinter import *
import Constants
from Game import *

class GameBoardGUI(Game):

    def __init__(self, master=None, gameType='CvP', markPlayer1 = 'X'):
        super().__init__(gameType, markPlayer1)
        self.master = master
        self.loadTextures()
        self.buildGameboard()
        self.buildTiles()
       
    def loadTextures(self):
        self.emptyTileImg = PhotoImage(file=texture.EMPTY_TILE_TEXTURE_PATH)
        self.crossImg = PhotoImage(file=texture.CROSS_TEXTURE_PATH)
        self.circleImg = PhotoImage(file=texture.CIRCLE_TEXTURE_PATH)
        self.gameboardImg = PhotoImage(file=texture.GAMEBOARD_TEXTURE_PATH)
        self.frameImg = PhotoImage(file=texture.GAMEBOARD_FRAME_TEXTURE_PATH)

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
           
        if self.isGameOver():
            self.disableAllTiles()

    def playerMoveIfGameIsntOver(self, x, y):
            markToPut = self.getMarkToPutAndSwitchCurrentPlayer()
            textureToPut = self.getTextureToPut(markToPut)
    
            self.changeTileTexture(self.tiles[x][y], textureToPut, markToPut)
            self.putMarkOnGameboard(x, y, markToPut)
            self.checkForWinner(markToPut)
            self.disableTile(self.tiles[x][y])

    def computerMoveIfGameIsntOver(self):
        if self.isGameOver():
            self.disableAllTiles()
        else:
            if self.isPlayerVsComputer() and self.isComputerCurrentPlayer():
                move = self.getComputerMove()
                markToPut = self.getMarkToPutAndSwitchCurrentPlayer()
                textureToPut = self.getTextureToPut(markToPut)
            
                self.changeTileTexture(self.tiles[move[0]][move[1]], textureToPut, markToPut)
                self.putMarkOnGameboard(move[0], move[1], markToPut)
                self.checkForWinner(markToPut)
                self.disableTile(self.tiles[move[0]][move[1]])

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

    def disableAllTiles(self):
        w, h = (3, 3)
        for i in range(w):
            for j in range(h):
                self.disableTile(self.tiles[i][j])
    
    def run(self):
        while not self.isGameOver():
            self.master.update_idletasks()
            self.master.update()
            self.computerMoveIfGameIsntOver()

    def deactivate(self):
        w, h = (3,3)
        for i in range(w):
            for j in range(h):
                self.tiles[i][j].grid_forget()
        
        self.frame.destroy()
        self.gameBoard.destroy()

if __name__ == "__main__":

    root = Tk()
    root.geometry("1920x1080")
    backgroundTexture = PhotoImage(file=texture.BACKGROUND_TEXTURE_PATH)
    background = Label(master=root, image=backgroundTexture).place(x=0,y=0)
    frameTexture = PhotoImage(file=texture.GAMEBOARD_FRAME_TEXTURE_PATH)
    frame = Label(master=root, bg=Constants.COLOR_BACKGROUND, image=frameTexture).place(relx=0.5, rely=0.5, anchor='center')
    gameBoard = GameBoardGUI(root)
    gameBoard.run()
   