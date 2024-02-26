# 3178 - Minimum Increment Operations to Make Array Beautiful
# Date: 2023-10-29
# Runtime: 696 ms, Memory: 30.6 MB
# Submission Id: 1086853607


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        nums = [max(0, k-num) for num in nums]
        n = len(nums)
        
        dp = nums[:3]
        for i in range(3, n):
            dp[i % 3] = nums[i] + min(dp)
            
        return min(dp)