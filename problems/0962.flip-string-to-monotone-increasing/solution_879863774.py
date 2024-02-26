# 0962 - Flip String to Monotone Increasing
# Date: 2023-01-17
# Runtime: 143 ms, Memory: 14.9 MB
# Submission Id: 879863774


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = ones = 0
        for ch in s:
            if ch == '0':
                ans = min(ans+1, ones)  # flip prev ones or itself
            else:
                ones += 1
        return ans