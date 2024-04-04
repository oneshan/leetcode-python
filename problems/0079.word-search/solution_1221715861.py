# 0079 - Word Search
# Date: 2024-04-03
# Runtime: 3707 ms, Memory: 16.5 MB
# Submission Id: 1221715861


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        len_r, len_c = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r == len_r or c < 0 or c == len_c or board[r][c] != word[i]:
                return False
            board[r][c] = '#'
            for nr, nc in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
                if backtrack(nr, nc, i+1):
                    return True
            board[r][c] = word[i]
            return False

        for r in range(len_r):
            for c in range(len_c):
                if backtrack(r, c, 0):
                    return True
        return False