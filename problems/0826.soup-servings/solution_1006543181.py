# 0826 - Soup Servings
# Date: 2023-07-29
# Runtime: 47 ms, Memory: 16.9 MB
# Submission Id: 1006543181


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        
        @cache
        def recur(i, j):
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0
            
            return (recur(i-4, j)
                    + recur(i-3, j-1)
                    + recur(i-2, j-2)
                    + recur(i-1, j-3)) / 4.0
        
        m = (n + 24) // 25
        return recur(m, m)