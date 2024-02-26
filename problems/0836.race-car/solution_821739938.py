# 0836 - Race Car
# Date: 2022-10-14
# Runtime: 624 ms, Memory: 14 MB
# Submission Id: 821739938


from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [float('inf')] * target
        for pos in range(3, target+1):
            step = pos.bit_length()
            if pos == (1<<step)-1:
                dp[pos] = step
                continue
            
            # A^(k-1) R A^(j) R
            for j in range(step-1):
                new_pos = pos - (1<<(step-1)) + (1<<j)
                dp[pos] = min(dp[pos], dp[new_pos] + (step-1) + j + 2)
            
            # A^k R
            new_pos = ((1<<step)-1) - pos
            if new_pos < pos:
                dp[pos] = min(dp[pos], dp[new_pos] + step + 1)

        return dp[target]