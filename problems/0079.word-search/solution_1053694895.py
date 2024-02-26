# 0079 - Word Search
# Date: 2023-09-19
# Runtime: 785 ms, Memory: 16.3 MB
# Submission Id: 1053694895


from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_r, len_c = len(board), len(board[0])
        n = len(word)
        
        # optimized
        def check_freq():
            counter = defaultdict(int)
            for r in range(len_r):
                for c in range(len_c):
                    counter[board[r][c]] += 1
            wc = defaultdict(int)
            for ch in word:
                wc[ch] += 1
                
            for ch in wc:
                if wc[ch] > counter[ch]:
                    return False
            return True
        
        def backtrack(r, c, idx):
            if idx == n:
                return True
            if 0 <= r < len_r and 0 <= c < len_c and board[r][c] == word[idx]:
                board[r][c] = '#'
                for nr, nc in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
                    if backtrack(nr, nc, idx + 1):
                        return True
                board[r][c] = word[idx]
            return False
        
        if not check_freq():
            return False
        
        for r in range(len_r):
            for c in range(len_c):
                if backtrack(r, c, 0):
                    return True
        return False