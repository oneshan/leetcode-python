# 1250 - Longest Common Subsequence
# Date: 2024-04-11
# Runtime: 1057 ms, Memory: 310.6 MB
# Submission Id: 1229237727


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            return max(dp(i+1, j), dp(i, j+1))
        
        return dp(0, 0)