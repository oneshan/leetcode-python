# 0494 - Target Sum
# Date: 2024-05-26
# Runtime: 196 ms, Memory: 43.8 MB
# Submission Id: 1268218672


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dp(i, curr):
            if i == n:
                return int(curr == target)
            return dp(i+1, curr+nums[i]) + dp(i+1, curr-nums[i])

        return dp(0, 0)