# 0198 - House Robber
# Date: 2023-09-20
# Runtime: 47 ms, Memory: 16.3 MB
# Submission Id: 1054386006


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(dp(i-2) + nums[i], dp(i-1))
        
        return dp(n-1)