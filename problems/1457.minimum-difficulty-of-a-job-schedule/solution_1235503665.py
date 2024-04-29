# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2024-04-18
# Runtime: 467 ms, Memory: 16.7 MB
# Submission Id: 1235503665


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        prev = [float('inf')] * n
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, jobDifficulty[i])
            prev[i] = curr_max

        for day in range(1, d):
            dp = [float('inf')] * n
            for i in range(n-1, day-1, -1):
                curr_max = 0
                for j in range(i, day-1, -1):
                    curr_max = max(curr_max, jobDifficulty[j])
                    dp[i] = min(dp[i], curr_max + prev[j-1])
            prev = dp

        return prev[-1]