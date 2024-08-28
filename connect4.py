import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, "|", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🟢":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+") 

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def getSpacePicked(col):
    for row in reversed(range(rows)):
        if gameBoard[row][col] == "":
            return (row, col)
    return None

def checkWin():
    for row in range(rows):
        for col in range(cols - 3):
            if gameBoard[row][col] == gameBoard[row][col + 1] == gameBoard[row][col + 2] == gameBoard[row][col + 3] != "":
                return True
    for row in range(rows - 3):
        for col in range(cols):
            if gameBoard[row][col] == gameBoard[row + 1][col] == gameBoard[row + 2][col] == gameBoard[row + 3][col] != "":
                return True
    for row in range(rows - 3):
        for col in range(cols - 3):
            if gameBoard[row][col] == gameBoard[row + 1][col + 1] == gameBoard[row + 2][col + 2] == gameBoard[row + 3][col + 3] != "":
                return True
    for row in range(3, rows):
        for col in range(cols - 3):
            if gameBoard[row][col] == gameBoard[row - 1][col + 1] == gameBoard[row - 2][col + 2] == gameBoard[row - 3][col + 3] != "":
                return True
    return False

turnCounter = 0
playerTurn = ["🔵", "🟢"]

while True:
    printGameBoard()
    currentPlayer = playerTurn[turnCounter % 2]
    print(f"\nPlayer {currentPlayer}'s turn")

    while True:
        column = input("Pick a column (A-G): ").upper()
        if column in possibleLetters:
            colIndex = possibleLetters.index(column)
            spacePicked = getSpacePicked(colIndex)
            if spacePicked is not None:
                modifyTurn(spacePicked, currentPlayer)
                break
            else:
                print("Column is full, pick another column.")
        else:
            print("Invalid input. Pick a column (A-G).")

    if checkWin():
        printGameBoard()
        print(f"\nPlayer {currentPlayer} wins!")
        break

    turnCounter += 1

    if turnCounter == rows * cols:
        printGameBoard()
        print("\nIt's a tie!")
        break

