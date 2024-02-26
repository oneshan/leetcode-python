# 0867 - New 21 Game
# Date: 2022-10-17
# Runtime: 387 ms, Memory: 29.2 MB
# Submission Id: 824411360


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        memo = {}
        def dfs(curr):
            if curr == k-1:
                return min(n-k+1, maxPts) / maxPts
            if curr > n:
                return 0
            if curr >= k:
                return 1
            if curr not in memo:
                memo[curr] = (dfs(curr+1)
                              - dfs(curr+1+maxPts) / maxPts
                              + dfs(curr+1) / maxPts)
            return memo[curr]
        
        return dfs(0)