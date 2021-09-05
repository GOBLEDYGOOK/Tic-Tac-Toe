
class MinimaxAi:

    def findBestMove(self, board, computerMark):
        self.computerMark = computerMark

        if self.computerMark == 'O':
            self.playerMark = 'X'
        else:
            self.playerMark = 'O'

        bestVal = -1000
        bestMove = ()
        rows = len(board)    
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):

                if board[i][j] == ' ':
                    board[i][j] = self.computerMark
                    moveVal = self.minimax(board, 0, False)
                    board[i][j] = ' '

                    if moveVal > bestVal:
                        bestVal = moveVal
                        bestMove = (i, j)

        return bestMove
                   
    def minimax(self, board, depth, isMaximizingPlayer):
        
        rows = len(board)    
        cols = len(board[0])
        score = self.checkBoard(board)

        if score == 10:
            return score

        if score == -10:
            return score

        if self.isMovesLeft(board) == False:
            return 0
        
        if isMaximizingPlayer == True:
            bestVal = -1000
            for i in range(rows):        
                for j in range(cols):
                    if board[i][j] == ' ':
                        board[i][j] = self.computerMark
                        bestVal = max(bestVal, self.minimax(board, depth+1, not isMaximizingPlayer))
                        board[i][j] = ' '
            return bestVal
        else:
            bestVal = 1000
            for i in range(rows):        
                for j in range(cols):
                    if board[i][j] == ' ':
                        board[i][j] = self.playerMark
                        bestVal = min(bestVal, self.minimax(board, depth+1, not isMaximizingPlayer))
                        board[i][j] = ' '
            return bestVal

                   

    def checkBoard(self, board):

        if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
            if board[0][0] == self.computerMark:
                return 10
            elif board[0][0] == self.playerMark:
                return -10
        
        if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
            if board[1][0] == self.computerMark:
                return 10
            elif board[1][0] == self.playerMark:
                return -10
        
        if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
            if board[2][0] == self.computerMark:
                return 10
            elif board[2][0] == self.playerMark:
                return -10
        
        if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
            if board[0][0] == self.computerMark:
                return 10
            elif board[0][0] == self.playerMark:
                return -10
        
        if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
            if board[0][1] == self.computerMark:
                return 10
            elif board[0][1] == self.playerMark:
                return -10
        
        if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
            if board[0][2] == self.computerMark:
                return 10
            elif board[0][2] == self.playerMark:
                return -10
        
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == self.computerMark:
                return 10
            elif board[0][0] == self.playerMark:
                return -10
        
        if board[2][0] == board[1][1]  and board[1][1] == board[0][2]:
            if board[2][0] == self.computerMark:
                return 10
            elif board[2][0] == self.playerMark:
                return -10

        if not self.isMovesLeft(board):
            return 0
        
    def isMovesLeft(self, board):
        rows = len(board)    
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ' ':
                    return True
        return False