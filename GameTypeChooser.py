from tkinter import *
from filePaths import texture


class GameTypeChooser:
    def __init__(self, master=None):
        self.master = master
        self.loadTextures()
        self.buildBackground()
        self.buildButtons()

    def loadTextures(self):
        self.pvpImg = PhotoImage(file=texture.PVP_BUTTON_TEXTURE_PATH)
        self.cvpImg = PhotoImage(file=texture.CVP_BUTTON_TEXTURE_PATH)
        self.choiceBackgroundImg = PhotoImage(file=texture.CHOICE_BACKGROUND_TEXTURE_PATH)

    def buildBackground(self):
        self.choiceBackground = Label(master=self.master, bg="black", image=self.choiceBackgroundImg)
        self.choiceBackground.grid_anchor('center')
    
    def buildButtons(self):
        self.gameTypeChoice = [
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='CvP', borderwidth=0, image=self.cvpImg, height=262, width=262),
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='PvP', borderwidth=0, image=self.pvpImg, height=262, width=262)
        ]
        self.gameTypeChoice[0]['command'] = lambda: self.clickGameTypeChoice(self.gameTypeChoice[0])
        self.gameTypeChoice[1]['command'] = lambda: self.clickGameTypeChoice(self.gameTypeChoice[1])
        
    def run(self):
        self.placeChooser()
        self.master.mainloop()

    def placeChooser(self):
        self.placeBackground()
        self.placeButtons()

    def placeBackground(self):
        self.choiceBackground.place(relx=0.5, rely=0.5, anchor='center')

    def placeButtons(self):
        self.gameTypeChoice[0].grid(row=0, column=0, padx=4, pady=4)
        self.gameTypeChoice[1].grid(row=0, column=1, padx=4, pady=4)
    
    def clickGameTypeChoice(self, button):
        self.gameType = button['text']
        self.deactivateGameTypeChoiceButtons()
        self.master.quit()

    def deactivateGameTypeChoiceButtons(self):
        self.gameTypeChoice[0].grid_forget()
        self.gameTypeChoice[1].grid_forget()
        self.choiceBackground.grid_forget()

    def getChoice(self):
        return self.gameType
    
if __name__ == "__main__":
    pass