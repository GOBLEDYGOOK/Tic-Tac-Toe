from tkinter import *
import WidgetCreator as wc
from filePaths import texture

class EndGameMenu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.playAgain = False
        self.panelImg = PhotoImage(file=texture.END_GAME_MENU_TEXTURE_PATH)
        self.panel = Label(master=self.master, bg='black', image=self.panelImg)
        self.panel.place(relx=0.5, rely=0.5, anchor='center')
        self.playAgainButton, self.playAgainButtonImg = wc.createWidget(master=self.panel, texturePath=texture.PLAY_AGAIN_BUTTON_TEXTURE_PATH, command=lambda: self.playAgainCommand())
        self.exitButton, self.exitButtonImg = wc.createWidget(master=self.panel, texturePath=texture.EXIT_BUTTON_TEXTURE_PATH, command=lambda: self.quit())
        self.playAgainButton.place(relx=0.5, rely=0.5, anchor='s')
        self.exitButton.place(relx=0.5, rely=0.5, anchor='n')

    def playAgainCommand(self):
        self.playAgain = True

    def quit(self):
        self.master.quit()
        self.master.destroy()

    def run(self):
         while True:
            self.master.update_idletasks()
            self.master.update()
            if self.playAgain:
                self.deactivate()
                break
    
    def deactivate(self):
        self.playAgainButton.grid_forget()
        self.exitButton.grid_forget()
        self.panel.destroy()
    