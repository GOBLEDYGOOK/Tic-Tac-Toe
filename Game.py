from Human import *
from Computer import *
from Gameboard import*

class Game:
    def __init__(self):
        self.player1 = Human(mark = 'X')
        self.player2 = Computer(mark = 'O')
        if self.player1.getMark() == 'X':
            self.currentPlayer = self.player1
        else:
            self.currentPlayer = self.player2
        self.gameboard = Gameboard()

    def isGameOver(self):
        return (self.gameboard.isBoardFull() or self.gameboard.isWinner())

    def getMarkToPutAndSwitchCurrentPlayer(self):
        if self.currentPlayer is self.player1:
            self.currentPlayer = self.player2
            return self.player1.getMark()
        else:
            self.currentPlayer = self.player1
            return self.player2.getMark()

    def putMarkOnGameboard(self, x, y, mark):
        self.gameboard.putMark(x, y, mark)
    
    def checkForWinner(self, mark):
        winner = self.gameboard.checkLines(mark)
        if self.gameboard.isWinner():
            print(f"{winner} has won!")
        elif self.gameboard.isBoardFull():
            print("There is a draw!")

    def isPlayerVsComputer(self):
        return isinstance(self.player2, Computer)

    def getComputerMove(self):
        return self.player2.bestMove(self.gameboard.getBoard())
        

    
    