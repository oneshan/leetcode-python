# 3033 - Apply Operations to Make Two Strings Equal
# Date: 2023-10-08
# Runtime: 53 ms, Memory: 16.2 MB
# Submission Id: 1069940371


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diff) & 1:
            return -1
        if len(diff) == 0:
            return 0
        
        n = len(diff)
        dp = [0] * (n+1)
        dp[1] = x/2
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + x/2, dp[i-2] + diff[i-1]-diff[i-2])

        return int(dp[-1])