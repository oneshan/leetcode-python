# 1400 - Find Winner on a Tic Tac Toe Game
# Date: 2022-09-16
# Runtime: 74 ms, Memory: 14 MB
# Submission Id: 801280586


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0 for _ in range(3)] for _ in range(3)]
        for idx, move in enumerate(moves):
            grid[move[0]][move[1]] = (idx & 1) + 1

        for x in range(3):
            if grid[x][0] and grid[x][0] == grid[x][1] == grid[x][2]:
                return 'A' if grid[x][0] == 1 else 'B'
            if grid[0][x] and grid[0][x] == grid[1][x] == grid[2][x]:
                return 'A' if grid[0][x] == 1 else 'B'

        if grid[1][1]:
            if grid[0][0] == grid[1][1] == grid[2][2]:
                return  'A' if grid[1][1] == 1 else 'B'
            if grid[0][2] == grid[1][1] == grid[2][0]:
                return  'A' if grid[1][1] == 1 else 'B'
        
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'