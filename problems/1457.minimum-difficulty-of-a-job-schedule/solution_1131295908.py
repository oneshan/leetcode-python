# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2023-12-29
# Runtime: 1519 ms, Memory: 17.4 MB
# Submission Id: 1131295908


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        
        dp = [float('inf')] * n + [0]
            
        for remains_d in range(1, d+1):
            new_dp = [float('inf')] * n + [0]
            for i in range(n-remains_d+1):
                curr_max = 0
                for j in range(i+1, n-remains_d+2):
                    curr_max = max(curr_max, jobDifficulty[j-1])
                    new_dp[i] = min(new_dp[i], curr_max + dp[j])
            dp = new_dp
        
        return dp[0]
        