
class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def updateScore(self):
        self.score = self.score+1

    def setMark(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark
    
    def getName(self):
        return self.name

    def getScore(self):
        return self.score