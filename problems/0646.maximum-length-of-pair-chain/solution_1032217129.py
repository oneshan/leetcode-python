# 0646 - Maximum Length of Pair Chain
# Date: 2023-08-26
# Runtime: 1608 ms, Memory: 16.9 MB
# Submission Id: 1032217129


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)