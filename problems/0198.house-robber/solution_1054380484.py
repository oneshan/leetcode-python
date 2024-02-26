# 0198 - House Robber
# Date: 2023-09-20
# Runtime: 35 ms, Memory: 16.2 MB
# Submission Id: 1054380484


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            return max(dp(i+1), nums[i] + dp(i+2))
        
        return dp(0)