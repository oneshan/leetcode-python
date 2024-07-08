# 0051 - N-Queens
# Date: 2024-05-19
# Runtime: 84 ms, Memory: 17.1 MB
# Submission Id: 1262060805


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        puzzle = [['.'] * n for _ in range(n)]

        def check(r, c):
            for i in range(n):
                if puzzle[i][c] == 'Q':
                    return False
                if c-i >= 0 and puzzle[r-i][c-i] == 'Q':
                    return False
                if c+i < n and puzzle[r-i][c+i] == 'Q':
                    return False
                if puzzle[r][i] == 'Q':
                    return False
            return True

        def backtrack(puzzle, r):
            if r == n:
                arr = [''.join(p) for p in puzzle]
                ans.append(arr)
                return
            for c in range(n):
                if check(r, c):
                    puzzle[r][c] = 'Q'
                    backtrack(puzzle, r+1)
                    puzzle[r][c] = '.'

        backtrack(puzzle, 0)
        return ans