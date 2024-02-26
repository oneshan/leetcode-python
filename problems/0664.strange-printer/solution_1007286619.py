# 0664 - Strange Printer
# Date: 2023-07-30
# Runtime: 327 ms, Memory: 19.3 MB
# Submission Id: 1007286619


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        @cache
        def recur(left, right):
            if left > right:
                return 0
            
            cost = 1 + recur(left, right-1)
            for i in range(left, right):
                if s[i] == s[right]:
                    cost = min(cost, recur(left, i-1) + recur(i, right-1))
            return cost
                    
        return recur(0, n-1)