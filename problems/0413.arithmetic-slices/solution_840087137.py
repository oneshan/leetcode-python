# 0413 - Arithmetic Slices
# Date: 2022-11-09
# Runtime: 64 ms, Memory: 14.2 MB
# Submission Id: 840087137


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 3:
            return 0
        
        dp = [0] * n
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
        return sum(dp)