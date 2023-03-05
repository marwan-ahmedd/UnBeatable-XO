from Board import Board
from ComputerMove import Computer

board = Board()
comp = Computer()
computer = "O"
player = "X"

while board.isMovesLeft:
    i, j = map(int, input("Enter i j separated by a space: ").split())

    if board.updateBoard(i, j, player):
        board.displayBoard()
    else:
        print("Invalid position, Please type a valid position: ")
        continue
    if board.isWinner():
        print("You have WON!")
        break
    
    b = board.getBoard()
    x, y = comp.findBestMove(b)
    
    board.updateBoard(x, y, computer)
    board.displayBoard()
    if board.isWinner():
        print("You Have LOST !")
        break
    