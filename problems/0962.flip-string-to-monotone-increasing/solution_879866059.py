# 0962 - Flip String to Monotone Increasing
# Date: 2023-01-17
# Runtime: 242 ms, Memory: 16.2 MB
# Submission Id: 879866059


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = sum([ch == '0' for ch in s])
        ones = 0
        
        ans = zeros + ones
        for ch in s:
            if ch == '0':
                zeros -= 1
            else:
                ones += 1
            ans = min(ans, zeros+ones)
        return ans