# 0091 - Decode Ways
# Date: 2022-10-14
# Runtime: 30 ms, Memory: 13.9 MB
# Submission Id: 822053474


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(1, len(s)):
            dp[i+1] = 0
            if s[i] != '0':
                dp[i+1] += dp[i]
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                dp[i+1] += dp[i-1]

        return dp[-1]