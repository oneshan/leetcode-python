# 0664 - Strange Printer
# Date: 2023-07-30
# Runtime: 328 ms, Memory: 19.1 MB
# Submission Id: 1007294594


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        @cache
        def recur(left, right):
            if left > right:
                return 0
            cost = 1 + recur(left+1, right)
            for i in range(left+1, right+1):
                if s[i] == s[left]:
                    cost = min(cost, recur(left, i-1) + recur(i+1, right))
            return cost
                    
        return recur(0, n-1)