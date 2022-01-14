from Human import *
from Computer import *
from Gameboard import*

class Game:
    def __init__(self, gameType):
        self.gameboard = Gameboard()
        if gameType == 'CvP':
            self.player1 = Human(name= "Player 1")
            self.player2 = Computer(name= "Player 2")
        elif gameType == 'PvP':
            self.player1 = Human(name= "Player 1")
            self.player2 = Human(name= "Player 2")

    def switchCurrentPlayer(self):
        if self.currentPlayer is self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def putMarkOnGameboard(self, x, y, mark):
        self.gameboard.putMark(x, y, mark)
    
    def checkForWinner(self, mark):
        self.gameboard.checkLines(mark)

    def updatePlayers(self, markPlayer1 = 'X'):
        self.player1.setMark(markPlayer1)
        self.player2.setMark(mark = 'O' if markPlayer1 == 'X' else 'X')
        self.setCurrentPlayer()
    
    def setCurrentPlayer(self):
        if self.player1.getMark() == 'X':
            self.currentPlayer = self.player1
        else:
            self.currentPlayer = self.player2

    def updateScoreIfIsWinner(self):
        if self.gameboard.isWinner():
            self.currentPlayer.updateScore()

    def isPlayerVsComputer(self):
        return isinstance(self.player2, Computer)

    def isComputerCurrentPlayer(self):
        return isinstance(self.currentPlayer, Computer)

    def isGameOver(self):
        return (self.gameboard.isBoardFull() or self.gameboard.isWinner())

    def getComputerMove(self):
        return self.player2.bestMove(self.gameboard.getBoard())

    def getMarkToPut(self):
        return self.currentPlayer.getMark()
        
    def getResult(self):
        winner = self.gameboard.getWinner()
        if self.gameboard.isWinner():
           return f"{winner} won!"
        elif self.gameboard.isBoardFull():
            return "Tie!"

    def getPlayerScores(self):
        return self.player1.getScore(), self.player2.getScore()

    def getPlayerNames(self):
        return self.player1.getName(), self.player2.getName()

    def reset(self):
        self.gameboard.reset()
    
    