# 0943 - Sum of Subarray Minimums
# Date: 2024-01-20
# Runtime: 327 ms, Memory: 21.4 MB
# Submission Id: 1151306112


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)
        stack = []
        dp = [0] * n
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
                
            if stack:
                dp[i] = dp[stack[-1]] + (i - stack[-1]) * arr[i]
            else:
                dp[i] = (i+1) * arr[i]
            stack.append(i)
        
        return sum(dp) % MOD