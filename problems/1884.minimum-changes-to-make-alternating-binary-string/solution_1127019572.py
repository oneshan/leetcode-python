# 1884 - Minimum Changes To Make Alternating Binary String
# Date: 2023-12-24
# Runtime: 46 ms, Memory: 17.2 MB
# Submission Id: 1127019572


class Solution:
    def minOperations(self, s: str) -> int:
        start1 = 0
        for idx, ch in enumerate(s):
            if idx & 1:
                if ch == '0':
                    start1 += 1
            else:
                if ch == '1':
                    start1 += 1
                    
        return min(start1, len(s) - start1)