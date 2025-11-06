from board import LemonBoard

if __name__ == "__main__":
    test = [[[8, True], [9, False], [4, False], [4, False], [4, False], [7, False]],
            [[9, False], [5, True], [3, False], [7, False], [1, False], [9, False]],
            [[2, False], [4, False], [2, False], [6, False], [4, False], [3, False]]]
    testBoard = LemonBoard(test)

    testBoard.printBoard()
    print()

    print(testBoard.checkRowVector(1, 2, 3))
    print(testBoard.checkRowVector(1, 4, 5))
    print(testBoard.checkRowVector(2, 3, 4))
    print(testBoard.checkColVector(0, 0, 2))
    print(testBoard.checkColVector(2, 0, 2))

