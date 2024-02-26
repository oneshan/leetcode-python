# 3312 - Number of Changing Keys
# Date: 2024-01-28
# Runtime: 40 ms, Memory: 16.5 MB
# Submission Id: 1158744175


class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        n = len(s)
        ans = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                ans += 1
        return ans