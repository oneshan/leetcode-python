# 0962 - Flip String to Monotone Increasing
# Date: 2023-01-17
# Runtime: 225 ms, Memory: 16 MB
# Submission Id: 879830097


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = sum([ch == '0' for ch in s])
        ans = m
        
        for ch in s:
            if ch == '0':
                m -= 1
            else:
                m += 1
            ans = min(ans, m)
            
        return ans