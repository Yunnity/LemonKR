from board import LemonBoard

def makeTestBoard(rows, cols, sequence):
    board = []
    for row in range(rows):
        currRow = []
        for col in range(cols):
            currRow.append([int(sequence[row * rows + col]), False])
        board.append(currRow)
    return board

if __name__ == "__main__":
    test = [[[8, True], [9, False], [4, False], [4, False], [4, False], [7, False]],
            [[9, False], [5, True], [3, False], [7, False], [1, False], [9, False]],
            [[2, False], [4, False], [2, False], [6, False], [4, False], [3, False]]]
    testBoard = LemonBoard(test)

    testBoard.printBoard()
    print()

    # print(testBoard.checkRowVector(1, 2, 3))
    # print(testBoard.checkRowVector(1, 4, 5))
    # print(testBoard.checkRowVector(2, 3, 4))
    # print(testBoard.checkColVector(0, 0, 2))
    # print(testBoard.checkColVector(2, 0, 2))
    # print()

    moves = testBoard.findAllMoves()
    for move in moves:
        print(move)
    print()

    a = makeTestBoard(3, 17, "863777574726869856979329723953972458177765338595876")
    testA = LemonBoard(a)
    testA.printBoard(showLemons=False)
    print()

    moves = testA.findAllMoves()
    for move in moves:
        print(move)
    print()
    testA.printBoard(showLemons=False)
    testA.printBoard()



