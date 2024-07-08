# 0416 - Partition Equal Subset Sum
# Date: 2024-05-24
# Runtime: 1535 ms, Memory: 492.6 MB
# Submission Id: 1266767091


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1

        n = len(nums)

        @cache
        def dp(i, curr):
            if curr == target:
                return True
            if i == n or curr > target:
                return False

            return dp(i+1, curr) or dp(i+1, curr + nums[i])

        return dp(0, 0)