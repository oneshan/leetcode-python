# 0416 - Partition Equal Subset Sum
# Date: 2024-05-24
# Runtime: 812 ms, Memory: 16.6 MB
# Submission Id: 1266773396


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False

        target = total >> 1
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[-1]