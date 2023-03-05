class Computer:
        
    def __minimax(self, board, isMax):
        computer, player = "O", "X"
        bestScore = self.__evaluate(board)
        
        # If player or computer won
        if bestScore == 10:
            return bestScore
        if bestScore == -10:
            return bestScore
        
        # If it is a tie
        if not self.__isMovesLeft(board):
            return 0
        
        # Computer (Maximizer's move)
        if isMax:
            best = float("-inf")
    
            for r in range(3) :         
                for c in range(3) :
                    # Check if cell is empty 
                    if board[r][c] == '_':
                        # Make the move 
                        board[r][c] = computer 
                        # Call minimax recursively and choose the maximum value 
                        best = max(best, self.__minimax(board, False))
                        # Undo the move 
                        board[r][c] = '_'
            return best
        
        # Player (Minimizer's move)
        else:
            best = float("inf") 
            for r in range(3) :         
                for c in range(3) :
                
                    # Check if cell is empty 
                    if board[r][c] == '_':
                        # Make the move 
                        board[r][c] = player 
                        # Call minimax recursively and choose the minimum value 
                        best = min(best, self.__minimax(board, True))
                        # Undo the move 
                        board[r][c] = '_'
            return best
        
        
    def findBestMove(self, board):
        computer, player = "O", "X"
        bestVal = -1000 
        bestMove = (-1, -1) 
    
        for r in range(3) :     
            for c in range(3) :
                # Check if cell is empty 
                if (board[r][c] == '_') : 
                    # Make the move 
                    board[r][c] = computer
                    moveVal = self.__minimax(board, False) 
                    # Undo the move 
                    board[r][c] = '_' 
                    # Get the maximum value
                    if moveVal > bestVal:                
                        bestMove = (r, c)
                        bestVal = moveVal
        return bestMove
    
    
    def __evaluate(self, board):
        computer, player = "O", "X"
        # Check rows
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == computer:
                    return 10
                elif board[row][0] == player:
                    return -10
        
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == computer: 
                    return 10
                elif board[0][col] == player:
                    return -10
        
        # Check diagonals
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        
            if board[0][0] == computer:
                return 10
            elif board[0][0] == player:
                return -10
    
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        
            if board[0][2] == computer:
                return 10
            elif board[0][2] == player:
                return -10
        return 0 # if no one won
    
    
    def __isMovesLeft(self, board):
        for r in range(3):
            for c in range(3):
                if board[r][c] == "_":
                    return True   
            