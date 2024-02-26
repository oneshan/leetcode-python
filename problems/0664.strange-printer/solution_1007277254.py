# 0664 - Strange Printer
# Date: 2023-07-30
# Runtime: 1605 ms, Memory: 21.3 MB
# Submission Id: 1007277254


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        @cache
        def recur(left, right):
            ans, j = float('inf'), -1
            for i in range(left, right):
                if s[i] != s[right] and j == -1:
                    j = i
                if j != -1:
                    ans = min(ans, 1 + recur(j, i) + recur(i+1, right))
            return ans if ans != float('inf') else 0
        
        return 1 + recur(0, n-1)