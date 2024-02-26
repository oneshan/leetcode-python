# 0494 - Target Sum
# Date: 2024-02-03
# Runtime: 188 ms, Memory: 44.1 MB
# Submission Id: 1164482542


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def recur(idx, curr_sum):
            if idx == n:
                return curr_sum == target
            return recur(idx+1, curr_sum - nums[idx]) + recur(idx+1, curr_sum + nums[idx])
        
        return recur(0, 0)