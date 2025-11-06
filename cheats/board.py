class LemonBoard(object):
    def __init__(self, board):
        self.lemonBoard = board
        # self.onlyNumsBoard = [[[col[0]] for col in row] for row in board]
        self.rowCount = len(board)
        if self.rowCount > 0:
            self.colsCount = len(board[0])
        else:
            self.colsCount = -1
    
    def printBoard(self, showLemons=True):
        if showLemons:
            board = self.lemonBoard
        else:
            board = self.onlyNumsBoard
        for row in range(self.rowCount):
            for col in range(self.colsCount):
                print(board[row][col], end="")
            print()
    
    def removeNums(self, topLeft, botRight):
        board = self.lemonBoard
        addedScore = 0
        for row in range(topLeft[0], botRight[0]+1):
            for col in range(topLeft[1], botRight[1]+1):
                addedScore += 1
                # if this number was a lemon number (worth 4)
                if board[row][col][1]:
                    addedScore += 3
                board[row][col] = [0, False]
        return addedScore

    def checkRowVector(self, row, left, right):
        board = self.lemonBoard
        sum = 0
        for col in range(left, right+1):
            sum += board[row][col][0]
        if sum == 10:
            return True
        return False

    def checkColVector(self, col, up, down):
        board = self.lemonBoard
        sum = 0
        for row in range(up, down+1):
            sum += board[row][col][0]
        if sum == 10:
            return True
        return False

    def checkMat(self, topLeft, botRight):
        board = self.lemonBoard
        sum = 0
        for row in range(topLeft[0], botRight[0]+1):
            for col in range(topLeft[1], botRight[1]+1):
                sum += board[row][col][0]
        if sum == 10:
            return True
        return False
    
    def findAllMoves(self):
        pass


    


