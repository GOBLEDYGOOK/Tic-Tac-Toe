from Player import *

class Human(Player):

    def __init__(self, mark):
        self.mark = mark
    
    def move(self, gameboard):
        pass

    def getMark(self):
        return self.mark
