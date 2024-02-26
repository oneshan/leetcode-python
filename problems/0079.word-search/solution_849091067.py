# 0079 - Word Search
# Date: 2022-11-24
# Runtime: 70 ms, Memory: 14.1 MB
# Submission Id: 849091067


from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_r, len_c = len(board), len(board[0])
        n = len(word)
        
        # optimized
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
        
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]
        
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