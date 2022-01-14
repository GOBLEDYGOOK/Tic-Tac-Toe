from tkinter import *
import WidgetCreator as wc
from filePaths import texture
from PIL import ImageTk, Image
import Constants

class MainMenu(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.titleImage = ImageTk.PhotoImage(file=texture.TITLE_TEXTURE_PATH)

        self.width, self.height = self.titleImage.width(), self.titleImage.height()
        self.canvas = Canvas(self.master, bg=Constants.COLOR_BACKGROUND, highlightthickness=0, width=self.width, height=self.height)
        self.canvas.place(relx=0.5, rely=0.15, anchor='center')
        self.canvas.create_image(0, 0, image=self.titleImage, anchor=NW)

        self.startGameButton, self.startGameButtonImg = wc.createWidget(self.master,texture.START_BUTTON_TEXTURE_PATH, command=lambda: self.startGameCommand())
        self.exitButton, self.exitButtonImg = wc.createWidget(self.master,texture.EXIT_BUTTON_TEXTURE_PATH, command= lambda: self.quit())
        self.startGameButton.place(relx=0.5, rely=0.40, anchor='center')
        self.exitButton.place(relx=0.5, rely=0.60, anchor='center')

    def startGameCommand(self):
        self.startGame = True
        self.master.quit()
        
    def quit(self):
        self.startGame = False
        self.master.quit()
        self.master.destroy()
        
    def run(self):
        self.startGame = False
        self.master.mainloop()
        if self.startGame:
            self.deactivate()
    
    def deactivate(self):
        self.startGameButton.place_forget()
        self.exitButton.place_forget()
        self.canvas.place_forget()
        
if __name__ == "__main__":
    root = Tk()
    root.geometry("1920x1080")
    
    filename = PhotoImage(file = "Graphics\\Background.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
   
    root.attributes('-fullscreen', True)
    
    menu = MainMenu(root)
    
    root.mainloop()