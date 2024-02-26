# 0413 - Arithmetic Slices
# Date: 2022-11-09
# Runtime: 72 ms, Memory: 14.1 MB
# Submission Id: 840088502


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        dp = ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp += 1
                ans += dp
            else:
                dp = 0
        return ans