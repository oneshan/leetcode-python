# 2855 - Maximum Number of Jumps to Reach the Last Index
# Date: 2024-06-03
# Runtime: 635 ms, Memory: 16.8 MB
# Submission Id: 1275856011


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if -target <= nums[j] - nums[i] <= target and dp[i] > -1:
                    dp[j] = max(dp[j], 1 + dp[i])

        return dp[-1]