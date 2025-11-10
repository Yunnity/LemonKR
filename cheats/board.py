class LemonBoard(object):
    def __init__(self, board):
        self.lemonBoard = board
        self.onlyNumsBoard = [[[col[0]] for col in row] for row in board]
        self.rowCount = len(board)
        if self.rowCount > 0:
            self.colCount = len(board[0])
        else:
            self.colCount = -1
    
    def printBoard(self, showLemons=True):
        if showLemons:
            board = self.lemonBoard
        else:
            board = self.onlyNumsBoard
        for row in range(self.rowCount):
            for col in range(self.colCount):
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
        """
        current implementation: essentially brute force, only optimization is we don't iterate
        over row or column vectors with a starting value of 0
        let r: number of rows, let c: number of columns
        To iterate over all of the values in a given row is cC2 (we essentially choose two numbers
        in the sequence of column indices, which we then set as our endpoints for our vector)
        To then iterate over all of the column vectors in a given column is rC2
        If we combined the two approaches (so that we iterate over all the column values
        alongside the rows), we could generalize everything as a matrix, which we should do eventually
        In this case, we would choose either columns or rows which will stay at rC2 or cC2, then the
        dimension we didn't choose will go to xC2 + x (e.g. rC2 + r) since we would check the individual
        rows or individual columns (didn't do it before since a single square can't be a solution)
        """
        board = self.lemonBoard
        # TODO: optimization, once we remove numbers from indices, no longer iterate over those indices
        # TODO: optimization, if the sum of a set of numbers exceeds 10, don't continue that line of checking

        rows = self.rowCount
        cols = self.colCount
        iterations = 0
        while True:
            # curious to see how many "iterations" are needed to clear a board on avg
            iterations += 1
            newMoves = False
            for row in range(rows):
                leftMost = 0
                while leftMost < cols and board[row][leftMost][0] == 0:
                    leftMost += 1
                # +1 since a single square by itself cannot sum to 1
                while (leftMost + 1) < cols:
                    for col in range(leftMost + 1, cols):
                        if self.checkRowVector(row, leftMost, col):
                            self.removeNums((row, leftMost), (row, col))
                            # self.printBoard()
                            yield [(row, leftMost), (row, col)]
                            newMoves = True
                    leftMost += 1
            for col in range(cols):
                topMost = 0
                while topMost < rows and board[topMost][col][0] == 0:
                    topMost += 1
                while (topMost + 1) < rows:
                    for row in range(topMost + 1, rows):
                        if self.checkColVector(col, topMost, row):
                            self.removeNums((topMost, col), (row, col))
                            # self.printBoard()
                            yield [(topMost, col), (row, col)]
                            newMoves = True
                    topMost += 1
            topRow = 0
            # the +1 here is such that if it were not included, we would iterate over col or row vectors again
            while (topRow + 1) < rows:
                # check all matrices with rows that span topRow to rows, excluding row vectors
                for row in range(topRow + 1, rows):
                    leftCol = 0
                    while (leftCol + 1) < cols:
                        for col in range(leftCol + 1, cols):
                            if self.checkMat((topRow, leftCol), (row, col)):
                                self.removeNums((topRow, leftCol), (row, col))
                                # self.printBoard()
                                yield [(topRow, leftCol), (row, col)]
                                newMoves = True
                        leftCol += 1
                topRow += 1
            if newMoves:
                iterations += 1
                continue
            break


    


