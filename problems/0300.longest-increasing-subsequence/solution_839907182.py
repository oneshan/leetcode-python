# 0300 - Longest Increasing Subsequence
# Date: 2022-11-09
# Runtime: 9755 ms, Memory: 14.3 MB
# Submission Id: 839907182


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)