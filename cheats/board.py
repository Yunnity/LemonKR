class LemonBoard(object):
    def __init__(self, board):
        self.lemonBoard = board
        self.onlyNumsBoard = [[[col[0]] for col in row] for row in board]
        self.rowCount = len(board)
        if self.rowCount > 0:
            self.colsCount = len(board[0])
        else:
            self.colsCount = -1
    
    def printBoard(self, showLemons=False):
        if showLemons:
            board = self.lemonBoard
        else:
            board = self.onlyNumsBoard
        for row in range(self.rowCount):
            for col in range(self.colsCount):
                print(board[row][col], end="")
            print()
    


