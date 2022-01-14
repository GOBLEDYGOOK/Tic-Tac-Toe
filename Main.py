from MainMenu import*
from GameTypeChooser import *
from GameBoardGUI import *
from EndGameMenu import *
from MarkTypeChooser import *

root = Tk()
root.geometry("1920x1080")
    
filename = PhotoImage(file = texture.BACKGROUND_TEXTURE_PATH)
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
   
root.attributes('-fullscreen', True)
    
menu = MainMenu(root)
menu.run()

gameTypeChooser = GameTypeChooser(master=root)
gameMarkChooser = MarkTypeChooser(master=root)
gameTypeChooser.run()
gameType = gameTypeChooser.getChoice()

endGameMenu = EndGameMenu(master=root)
gameBoard = GameBoardGUI(master=root, gameType=gameType)
while True:
    gameMarkChooser.run()
    mark = gameMarkChooser.getChoice()
    gameBoard.run(mark)
    result = gameBoard.getResult()
    endGameMenu.run(result)
    if not endGameMenu.playAgain: break
    gameBoard.deactivate()    
