# 1400 - Find Winner on a Tic Tac Toe Game
# Date: 2022-09-16
# Runtime: 79 ms, Memory: 14 MB
# Submission Id: 801295387


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        player = 1
        for row, col in moves:
            rows[row] += player
            cols[col] += player
            
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player
            
            for line in (rows[row], cols[col], diag, anti_diag):
                if abs(line) == n:
                    return 'A' if line > 0 else 'B'
                
            player *= -1
        
        return 'Pending' if len(moves) < n * n else 'Draw'