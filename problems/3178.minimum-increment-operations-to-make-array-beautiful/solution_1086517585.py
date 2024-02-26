# 3178 - Minimum Increment Operations to Make Array Beautiful
# Date: 2023-10-29
# Runtime: 732 ms, Memory: 33.3 MB
# Submission Id: 1086517585


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        nums = [max(0, k-num) for num in nums]
        n = len(nums)
        
        dp = [0] * n
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2]
        for i in range(3, n):
            dp[i] = nums[i] + min(dp[i-1], dp[i-2], dp[i-3])
            
        return min(dp[-1], dp[-2], dp[-3])