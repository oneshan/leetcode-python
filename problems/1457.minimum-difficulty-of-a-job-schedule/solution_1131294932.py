# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2023-12-29
# Runtime: 1430 ms, Memory: 17.6 MB
# Submission Id: 1131294932


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[float('inf')] * (n+1) for _ in range(d+1)]
        for i in range(d+1):
            dp[i][-1] = 0
            
        for remains_d in range(1, d+1):
            for i in range(n-remains_d+1):
                curr_max = 0
                for j in range(i+1, n-remains_d+2):
                    curr_max = max(curr_max, jobDifficulty[j-1])
                    dp[remains_d][i] = min(dp[remains_d][i],
                                           curr_max + dp[remains_d-1][j])
        
        return dp[d][0]
        