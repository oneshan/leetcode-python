# 0712 - Minimum ASCII Delete Sum for Two Strings
# Date: 2023-07-31
# Runtime: 409 ms, Memory: 16.4 MB
# Submission Id: 1008319489


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        if n1 < n2:
            return self.minimumDeleteSum(s2, s1)
        
        dp = [0] * (n2+1)
        for j in range(n2):
            dp[j+1] = dp[j] + ord(s2[j])
        
        for i in range(n1):
            diag, dp[0] = dp[0], dp[0] + ord(s1[i])
            for j in range(n2):
                if s1[i] == s2[j]:
                    tmp = diag
                else:
                    tmp = min(dp[j+1] + ord(s1[i]),
                              dp[j] + ord(s2[j]))
                diag, dp[j+1] = dp[j+1], tmp
                    
        return dp[-1]