# 0289 - Game of Life
# Date: 2024-02-21
# Runtime: 39 ms, Memory: 16.7 MB
# Submission Id: 1181637734


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        len_r, len_c = len(board), len(board[0])

        def get_live(r, c):
            lives = 0
            for nr in (r-1, r, r+1):
                for nc in (c-1, c, c+1):
                    if nr == r and nc == c:
                        continue
                    if nr in (-1, len_r) or nc in (-1, len_c):
                        continue
                    if board[nr][nc] & 1:
                        lives += 1
            return lives

        for r in range(len_r):
            for c in range(len_c):
                live = get_live(r, c)
                if board[r][c] == 1 and live not in (2, 3):
                    board[r][c] = 3  # live -> die
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 2  # die -> live
        
        for r in range(len_r):
            for c in range(len_c):
                if board[r][c] > 1:
                    board[r][c] ^= 3