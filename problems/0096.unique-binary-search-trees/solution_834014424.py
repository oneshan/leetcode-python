# 0096 - Unique Binary Search Trees
# Date: 2022-10-31
# Runtime: 64 ms, Memory: 14 MB
# Submission Id: 834014424


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        # G(n) = Sum(F(i,n)) = Sum(G(i-1)*G(n-i))
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
    
        return dp[n]