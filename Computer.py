from Player import *
from MinimaxAi import *

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.ai = MinimaxAi()

    def bestMove(self, board):
        bestMove = self.ai.findBestMove(board, self.mark)   
        board[bestMove[0]][bestMove[1]] = self.mark
        return bestMove