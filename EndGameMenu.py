from tkinter import *
import WidgetCreator as wc
from filePaths import texture
import Constants

class EndGameMenu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.panelImg = PhotoImage(file=texture.END_GAME_MENU_TEXTURE_PATH)
        self.panel = Label(master=self.master, bg='black', image=self.panelImg)
        self.resultToDisplay = Label(master=self.panel, bg = Constants.COLOR_BACKGROUND, font = "Helvetica 34 bold")
        self.playAgainButton, self.playAgainButtonImg = wc.createWidget(master=self.panel, texturePath=texture.PLAY_AGAIN_BUTTON_TEXTURE_PATH, command=lambda: self.playAgainCommand())
        self.exitButton, self.exitButtonImg = wc.createWidget(master=self.panel, texturePath=texture.EXIT_BUTTON_TEXTURE_PATH, command=lambda: self.quit())
       
    def playAgainCommand(self):
        self.playAgain = True
        self.master.quit()

    def quit(self):
        self.playAgain = False
        self.master.quit()
        self.master.destroy()

    def run(self, result):
        self.result = result
        self.playAgain = False
        self.placeMenu()

        self.master.mainloop()
        if self.playAgain:
            self.deactivate()

    def placeMenu(self):
        self.panel.place(relx=0.75, rely=0.5, anchor='w')
        self.resultToDisplay["text"] = self.result
        self.resultToDisplay.place(relx=0.5, rely=0.025, anchor='n')
        self.playAgainButton.place(relx=0.5, rely=0.5, anchor='s')
        self.exitButton.place(relx=0.5, rely=0.5, anchor='n')

    def deactivate(self):
        self.playAgainButton.grid_forget()
        self.exitButton.grid_forget()
        self.panel.place_forget()
    