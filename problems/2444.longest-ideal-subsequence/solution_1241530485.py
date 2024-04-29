# 2444 - Longest Ideal Subsequence
# Date: 2024-04-25
# Runtime: 1537 ms, Memory: 17.4 MB
# Submission Id: 1241530485


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for ch in s:
            i = ord(ch) - ord('a')
            curr = 0
            for j in range(26):
                if abs(i-j) <= k:
                    curr = max(curr, dp[j])
            dp[i] = max(dp[i], curr+1)
        return max(dp)