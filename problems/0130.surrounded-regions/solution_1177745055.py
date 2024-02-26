# 0130 - Surrounded Regions
# Date: 2024-02-17
# Runtime: 119 ms, Memory: 17.8 MB
# Submission Id: 1177745055


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        len_r, len_c = len(board), len(board[0])

        def traverse(row, col):
            stack = [(row, col)]
            board[row][col] = 'B'
            while stack:
                r, c = stack.pop()
                for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                    next_r, next_c = r+dr, c+dc
                    if 0 <= next_r < len_r and 0 <= next_c < len_c and board[next_r][next_c] == 'O':
                        stack.append((next_r, next_c))
                        board[next_r][next_c] = 'B'

        for r in range(len_r):
            if board[r][0] == 'O':
                traverse(r, 0)
            if board[r][len_c-1] == 'O':
                traverse(r, len_c-1)
        for c in range(len_c):
            if board[0][c] == 'O':
                traverse(0, c)
            if board[len_r-1][c] == 'O':
                traverse(len_r-1, c)

        for r in range(len_r):
            for c in range(len_c):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'B':
                    board[r][c] = 'O'