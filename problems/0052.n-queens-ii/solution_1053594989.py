# 0052 - N-Queens II
# Date: 2023-09-19
# Runtime: 80 ms, Memory: 16.2 MB
# Submission Id: 1053594989


class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def check(r, c, arr):
            for row, col in arr:
                if row == r or col == c or abs(row-r) == abs(col-c):
                    return False
            return True
        
        def backtrack(arr, r):
            if r == n:
                return 1
            count = 0
            for c in range(n):
                if check(r, c, arr):
                    arr.append((r, c))
                    count += backtrack(arr, r+1)
                    arr.pop()
            return count
        
        
        return backtrack([], 0)