from tkinter import *
import Constants
from PIL import Image

def createWidget(master, texturePath, command=None):
    buttonImg = PhotoImage(master=master, file=texturePath)
    button = Button(master,
                    bg=Constants.COLOR_BACKGROUND,
                    activebackground=Constants.COLOR_BACKGROUND,
                    image = buttonImg, 
                    borderwidth=0, 
                    command=command)

    return button, buttonImg
