from tkinter import *
from filePaths import texture

class MarkTypeChooser:
    def __init__(self, master=None):
        self.master = master
        self.loadTextures()
        self.buildBackground()
        self.buildButtons()

    def loadTextures(self):
        self.crossImg = PhotoImage(file=texture.CROSS_TEXTURE_PATH)
        self.circleImg = PhotoImage(file=texture.CIRCLE_TEXTURE_PATH)
        self.choiceBackgroundImg = PhotoImage(file=texture.CHOICE_BACKGROUND_TEXTURE_PATH)

    def buildBackground(self):
        self.choiceBackground = Label(master=self.master, bg="black", image=self.choiceBackgroundImg)
        self.choiceBackground.grid_anchor('center')
    
    def buildButtons(self):
    
        self.markChoice = [
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='X', borderwidth=0, image=self.crossImg, height=262, width=262),
            Button(master=self.choiceBackground, bg="black", activebackground="black", text='O', borderwidth=0, image=self.circleImg, height=262, width=262)
        ]
        self.markChoice[0]['command'] = lambda: self.clickMarkChoice(self.markChoice[0])
        self.markChoice[1]['command'] = lambda: self.clickMarkChoice(self.markChoice[1])

    def run(self):
        self.placeChooser()
        self.master.mainloop()

    def placeChooser(self):
        self.placeBackground()
        self.placeButtons()

    def placeBackground(self):
        self.choiceBackground.place(relx=0.5, rely=0.5, anchor='center')

    def placeButtons(self):
        self.markChoice[0].grid(row=0, column=0, padx=4, pady=4)
        self.markChoice[1].grid(row=0, column=1, padx=4, pady=4)
    
    def clickMarkChoice(self, button):
        self.mark = button['text']
        self.deactivateMarkChoiceButtonsAndBackground()
        self.master.quit()

    def deactivateMarkChoiceButtonsAndBackground(self):
        self.markChoice[0].grid_forget()
        self.markChoice[1].grid_forget()
        self.choiceBackground.grid_forget()

    def getChoice(self):
        return self.mark
    