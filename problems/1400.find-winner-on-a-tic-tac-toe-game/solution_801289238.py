# 1400 - Find Winner on a Tic Tac Toe Game
# Date: 2022-09-16
# Runtime: 88 ms, Memory: 14 MB
# Submission Id: 801289238


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        grid = [[0] * n for _ in range(n)]
        
        def check_row(y, player):
            return all(grid[x][y] == player for x in range(n))
        
        def check_col(x, player):
            return all(grid[x][y] == player for y in range(n))
        
        def check_diag(player):
            return all(grid[x][x] == player for x in range(n))
        
        def check_anti_diag(player):
            return all(grid[x][n-x-1] == player for x in range(n))
        
        for idx, (row, col) in enumerate(moves):
            player = ('A', 'B')[idx & 1]
            grid[row][col] = player
            if check_row(col, player) or check_col(row, player):
                return player
            if row == col and check_diag(player):
                return player
            if row + col == n - 1 and check_anti_diag(player):
                return player
        
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'