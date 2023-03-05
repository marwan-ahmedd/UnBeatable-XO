class Board:
    def __init__(self):
        self.__board = [
        [ '_', '_', '_' ], 
        [ '_', '_', '_' ], 
        [ '_', '_', '_' ]]
    
    def updateBoard(self, x, y, symbol):
        if (not (x < 0 or x > 2 or y < 0 or y > 2) and (self.__board[x][y] == "_")):
            self.__board[x][y] = symbol.upper()
            return True
        return False
    
    def isWinner(self):
        for i in range(3):
            for j in range(3):
                if (self.__board[i][0] == self.__board[i][1] and self.__board[i][1] == self.__board[i][2] and self.__board[i][2] != "_") or \
                (self.__board[0][j] == self.__board[1][j] and self.__board[1][j] == self.__board[2][j] and self.__board[2][j] != "_") or \
                (self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2] and self.__board[2][2] != "_") or \
                (self.__board[0][2] == self.__board[1][1] and self.__board[1][1] == self.__board[2][0] and self.__board[2][0] != "_"):
                    return True
        return False
    
    def isMovesLeft(self):
        for r in range(3):
            for c in range(3):
                if self.__board[r][c] == "_":
                    return True   
            
        
    def displayBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.__board[i][j], end=" ")
            print()
        print()
        
            
    def getBoard(self):
        return self.__board
        