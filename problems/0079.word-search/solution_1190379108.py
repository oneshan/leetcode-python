# 0079 - Word Search
# Date: 2024-03-01
# Runtime: 3766 ms, Memory: 16.6 MB
# Submission Id: 1190379108


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        len_r, len_c = len(board), len(board[0])

        def backtrack(idx, r, c):
            if idx == n:
                return True
            if 0 <= r < len_r and 0 <= c < len_c and board[r][c] == word[idx]:
                board[r][c] = '#'
                for nr, nc in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
                    if backtrack(idx+1, nr, nc):
                        return True
                board[r][c] = word[idx]
            return False

        for r in range(len_r):
            for c in range(len_c):
                if backtrack(0, r, c):
                    return True
        return False