from tkinter import *
from filePaths import texture
from GameBoardGUI import *
from EndGameMenu import *

class GameTypeChooser:
    def __init__(self, master=None):
        self.master = master
        self.gameIsBuilt = False
        self.loadTextures()
        self.buildBackground()
        self.buildButtons()

    def loadTextures(self):
        self.emptyTileImg = PhotoImage(file=texture.EMPTY_TILE_TEXTURE_PATH)
        self.crossImg = PhotoImage(file=texture.CROSS_TEXTURE_PATH)
        self.circleImg = PhotoImage(file=texture.CIRCLE_TEXTURE_PATH)
        self.pvpImg = PhotoImage(file=texture.PVP_BUTTON_TEXTURE_PATH)
        self.cvpImg = PhotoImage(file=texture.CVP_BUTTON_TEXTURE_PATH)
        self.choiceBackgroundImg = PhotoImage(file=texture.CHOICE_BACKGROUND_TEXTURE_PATH)
    
    def buildBackground(self):
        self.choiceBackground = Label(master=self.master, bg="black", image=self.choiceBackgroundImg)
        self.choiceBackground.grid_anchor('center')
        self.choiceBackground.place(relx=0.5, rely=0.5, anchor='center')

    def buildButtons(self):
        self.gameTypeChoice = [
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='CvP', borderwidth=0, image=self.cvpImg, height=262, width=262),
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='PvP', borderwidth=0, image=self.pvpImg, height=262, width=262)
        ]
        self.gameTypeChoice[0]['command'] = lambda: self.clickGameTypeChoice(self.gameTypeChoice[0])
        self.gameTypeChoice[1]['command'] = lambda: self.clickGameTypeChoice(self.gameTypeChoice[1])
        self.gameTypeChoice[0].grid(row=0, column=0, padx=4, pady=4)
        self.gameTypeChoice[1].grid(row=0, column=1, padx=4, pady=4)

        self.markChoice = [
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='X', borderwidth=0, image=self.crossImg, height=262, width=262),
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='O', borderwidth=0, image=self.circleImg, height=262, width=262)
        ]
        self.markChoice[0]['command'] = lambda: self.clickMarkChoice(self.markChoice[0])
        self.markChoice[1]['command'] = lambda: self.clickMarkChoice(self.markChoice[1])

    def clickGameTypeChoice(self, button):
        self.gameType = button['text']
        self.deactivateGameTypeChoiceButtons()
        self.nextChoice()
    
    def clickMarkChoice(self, button):
        self.mark = button['text']
        self.deactivateMarkChoiceButtonsAndBackground()
        self.gameIsBuilt = True

    def deactivateGameTypeChoiceButtons(self):
        self.gameTypeChoice[0].grid_forget()
        self.gameTypeChoice[1].grid_forget()
        

    def nextChoice(self):
        self.markChoice[0].grid(row=0, column=0, padx=4, pady=4)
        self.markChoice[1].grid(row=0, column=1, padx=4, pady=4)

    def deactivateMarkChoiceButtonsAndBackground(self):
        self.markChoice[0].grid_forget()
        self.markChoice[1].grid_forget()
        self.choiceBackground.destroy()

    def run(self):
        while self.isGameNotReadyToStart():
            self.master.update_idletasks()
            self.master.update()

    def isGameNotReadyToStart(self):
        return not self.gameIsBuilt

    def getChoices(self):
        return self.gameType, self.mark
    
if __name__ == "__main__":
    root = Tk()
    root.geometry("1920x1080")
    backgroundTexture = PhotoImage(file=texture.BACKGROUND_TEXTURE_PATH)
    background = Label(master=root, image=backgroundTexture).place(x=0,y=0)
    while True:
        gameChooser = GameTypeChooser(master=root)
        gameChooser.run()
        gameType, mark = gameChooser.getChoices()
        gameBoard = GameBoardGUI(root, gameType, mark)
        gameBoard.run()
        endGameMenu = EndGameMenu(root)
        endGameMenu.run()
        gameBoard.deactivate()
       

        