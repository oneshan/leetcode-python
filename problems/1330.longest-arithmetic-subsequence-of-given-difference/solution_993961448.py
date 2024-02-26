# 1330 - Longest Arithmetic Subsequence of Given Difference
# Date: 2023-07-14
# Runtime: 574 ms, Memory: 30 MB
# Submission Id: 993961448


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for num in arr:
            dp[num] = 1 + dp.get(num - difference, 0)
            ans = max(ans, dp[num])
        return ans