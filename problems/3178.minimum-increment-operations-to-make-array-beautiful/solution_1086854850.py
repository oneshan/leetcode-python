# 3178 - Minimum Increment Operations to Make Array Beautiful
# Date: 2023-10-29
# Runtime: 704 ms, Memory: 30.7 MB
# Submission Id: 1086854850


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)        
        dp = [0] * 3
        for i in range(n):
            dp[i % 3] = max(0, k-nums[i]) + min(dp)
            
        return min(dp)