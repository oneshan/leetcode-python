# 2883 - Partition String Into Minimum Beautiful Substrings
# Date: 2024-01-16
# Runtime: 48 ms, Memory: 17.5 MB
# Submission Id: 1147899908


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        pow5 = set(pow(5, i) for i in range(7))
        n = len(s)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            if s[i] == '0':
                return float('inf')
            
            res, curr = float('inf'), 0
            for j in range(i, n):
                curr = (curr << 1) + (s[j] == '1')
                if curr in pow5:
                    res = min(res, 1 + dp(j+1))
            return res
        
        ans = dp(0)
        return ans if ans != float('inf') else -1