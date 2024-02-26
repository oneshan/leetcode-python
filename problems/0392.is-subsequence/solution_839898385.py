# 0392 - Is Subsequence
# Date: 2022-11-09
# Runtime: 126 ms, Memory: 14.9 MB
# Submission Id: 839898385


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        
        if len_s == 0:
            return True
        
        dp = [ [0] * (len_t+1) for _ in range(len_s+1)]
        for col in range(1, len_t+1):
            for row in range(1, len_s+1):
                if s[row-1] == t[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
            
            if dp[len_s][col] == len_s:
                return True

        return False