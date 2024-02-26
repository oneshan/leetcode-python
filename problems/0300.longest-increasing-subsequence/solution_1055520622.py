# 0300 - Longest Increasing Subsequence
# Date: 2023-09-21
# Runtime: 2461 ms, Memory: 16.5 MB
# Submission Id: 1055520622


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)