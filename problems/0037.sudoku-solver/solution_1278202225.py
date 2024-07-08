# 0037 - Sudoku Solver
# Date: 2024-06-05
# Runtime: 127 ms, Memory: 16.6 MB
# Submission Id: 1278202225


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        def set_num(r, c, d):
            rows[r] |= (1 << d)
            cols[c] |= (1 << d)
            boxes[(r//3)*3+(c//3)] |= (1 << d)
            board[r][c] = str(d)

        def unset_num(r, c, d):
            rows[r] &= ~(1 << d)
            cols[c] &= ~(1 << d)
            boxes[(r//3)*3+(c//3)] &= ~(1 << d)
            board[r][c] = '.'

        def is_valid(r, c, d):
            return (
                rows[r] & (1 << d) == 0
                and cols[c] & (1 << d) == 0
                and boxes[(r//3)*3+(c//3)] & (1 << d) == 0
            )

        def backtrack(num):
            if num == n * n:
                return True
            
            r, c = divmod(num, n)
            
            if board[r][c] != '.':
                return backtrack(num+1)
            
            for i in range(1, 10):
                if is_valid(r, c, i):
                    set_num(r, c, i)
                    if backtrack(num+1):
                        return True
                    unset_num(r, c, i)
            return False

        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    digit = int(board[r][c])
                    set_num(r, c, digit)

        backtrack(0)