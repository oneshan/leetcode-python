# 0079 - Word Search
# Date: 2022-11-24
# Runtime: 4150 ms, Memory: 13.9 MB
# Submission Id: 849088124


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_r, len_c = len(board), len(board[0])
        n = len(word)
        
        def backtrack(r, c, idx):
            if idx == n:
                return True
            if r < 0 or r == len_r or c < 0 or c == len_c or board[r][c] != word[idx]:
                return False
            
            board[r][c] = '#'
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                if backtrack(r+dx, c+dy, idx+1):
                    return True
            board[r][c] = word[idx]
            return False
        
        for r in range(len_r):
            for c in range(len_c):
                if backtrack(r, c, 0):
                    return True
        return False