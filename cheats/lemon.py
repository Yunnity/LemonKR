from board import LemonBoard

if __name__ == "__main__":
    test = [[[8, True], [9, False], [4, False], [4, False], [4, False], [7, False]],
            [[9, False], [5, True], [3, False], [7, False], [1, False], [9, False]],
            [[2, False], [4, False], [2, False], [6, False], [4, False], [3, False]]]
    testBoard = LemonBoard(test)

    testBoard.printBoard()
