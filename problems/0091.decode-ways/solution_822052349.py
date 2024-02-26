# 0091 - Decode Ways
# Date: 2022-10-14
# Runtime: 55 ms, Memory: 14 MB
# Submission Id: 822052349


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(dp)):
            dp[i] = 0
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'):
                dp[i] += dp[i-2]

        return dp[-1]