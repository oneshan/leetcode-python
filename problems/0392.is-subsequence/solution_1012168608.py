# 0392 - Is Subsequence
# Date: 2023-08-04
# Runtime: 79 ms, Memory: 17.3 MB
# Submission Id: 1012168608


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        len_s, len_t = len(s), len(t)
        if len_s > len_t:
            return False
        
        dp = [[0] * (len_t+1) for _ in range(len_s+1)]
        for r in range(len_s):
            for c in range(len_t):
                if s[r] == t[c]:
                    dp[r+1][c+1] = 1 + dp[r][c]
                else:
                    dp[r+1][c+1] = max(dp[r][c+1], dp[r+1][c])
            if dp[len_s][c+1] == len_s:
                return True
        return False