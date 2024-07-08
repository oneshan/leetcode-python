# 0079 - Word Search
# Date: 2024-05-19
# Runtime: 43 ms, Memory: 16.7 MB
# Submission Id: 1261987615


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        len_r, len_c = len(board), len(board[0])

        # optimized
        bc = defaultdict(int)
        for r in range(len_r):
            for c in range(len_c):
                bc[board[r][c]] += 1

        wc = Counter(word)
        for ch in wc:
            if wc[ch] > bc[ch]:
                return False
        if bc[word[0]] > bc[word[-1]]:
            word = word[::-1]

        def backtrack(r, c, i):
            if i == n:
                return True
            if not (0 <= r < len_r and 0 <= c < len_c):
                return False
            if board[r][c] != word[i]:
                return False

            origin_ch = board[r][c]
            board[r][c] = '#'
            for nr, nc in (r-1, c), (r+1, c), (r, c+1), (r, c-1):
                if backtrack(nr, nc, i+1):
                    return True
            board[r][c] = origin_ch
            return False

        
        for r in range(len_r):
            for c in range(len_c):
                if backtrack(r, c, 0):
                    return True
        return False