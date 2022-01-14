
class Gameboard:

    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.winner = " "

    def checkLines(self, mark):

        if self.board[0][0] == mark and self.board[0][1] == mark and self.board[0][2]  == mark:
            self.winner = mark
        
        if self.board[1][0] == mark and self.board[1][1] == mark and self.board[1][2]  == mark:
            self.winner = mark
        
        if self.board[2][0] == mark and self.board[2][1] == mark and self.board[2][2]  == mark:
            self.winner = mark
        
        if self.board[0][0] == mark and self.board[1][0] == mark and self.board[2][0]  == mark:
            self.winner = mark
        
        if self.board[0][1] == mark and self.board[1][1] == mark and self.board[2][1]  == mark:
            self.winner = mark
        
        if self.board[0][2] == mark and self.board[1][2] == mark and self.board[2][2]  == mark:
            self.winner = mark
        
        if self.board[0][0] == mark and self.board[1][1] == mark and self.board[2][2]  == mark:
            self.winner = mark
        
        if self.board[2][0] == mark and self.board[1][1] == mark and self.board[0][2]  == mark:
            self.winner = mark
        
        if self.winner == ' ' and self.isBoardFull():
            self.winner = 'draw'

    
    def isBoardFull(self):
        w, h = (3, 3)
        for i in range(w):
            for j in range(h):
                if self.board[i][j] == ' ':
                    return False
        return True

    def isWinner(self):
        if self.winner == ' ' or self.winner == 'draw':
            return False
        else:
            return True

    def putMark(self, x, y, mark):
        self.board[x][y] = mark

    def getBoard(self):
        return self.board

    def getWinner(self):
        return self.winner

    def reset(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.winner = " "
        
if __name__ == "__main__":
    pass