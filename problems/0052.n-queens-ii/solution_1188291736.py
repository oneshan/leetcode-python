# 0052 - N-Queens II
# Date: 2024-02-28
# Runtime: 62 ms, Memory: 16.5 MB
# Submission Id: 1188291736


class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def check(r, c, arr):
            for row, col in arr:
                if row == r or col == c or abs(row-r) == abs(col-c):
                    return False
            return True

        def backtrack(r, arr):
            if r == n:
                self.ans += 1
                return

            for c in range(n):
                if check(r, c, arr):
                    arr.append((r,c))
                    backtrack(r+1, arr)
                    arr.pop()

        self.ans = 0
        backtrack(0, [])
        return self.ans