# 0416 - Partition Equal Subset Sum
# Date: 2024-05-24
# Runtime: 1615 ms, Memory: 581.4 MB
# Submission Id: 1266765405


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        n = len(nums)

        @cache
        def dp(i, curr):
            if i == n:
                return curr == total - curr
            
            return dp(i+1, curr) or dp(i+1, curr + nums[i])

        return dp(0, 0)