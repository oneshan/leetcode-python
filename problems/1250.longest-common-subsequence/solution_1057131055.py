# 1250 - Longest Common Subsequence
# Date: 2023-09-23
# Runtime: 586 ms, Memory: 41.6 MB
# Submission Id: 1057131055


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1, len_2 = len(text1), len(text2)
        
        dp = [ [0] * (len_2+1) for _ in range(len_1 + 1)]
        
        for row in range(len_1):
            for col in range(len_2):
                if text1[row] == text2[col]:
                    dp[row+1][col+1] = dp[row][col] + 1
                else:
                    dp[row+1][col+1] = max(dp[row+1][col], dp[row][col+1])
        
        return dp[-1][-1]