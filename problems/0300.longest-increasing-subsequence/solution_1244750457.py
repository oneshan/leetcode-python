# 0300 - Longest Increasing Subsequence
# Date: 2024-04-29
# Runtime: 1809 ms, Memory: 17 MB
# Submission Id: 1244750457


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)