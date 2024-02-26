# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2023-12-29
# Runtime: 98 ms, Memory: 17.4 MB
# Submission Id: 1131306356


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [float('inf')] * n

        for day in range(d):
            new_dp = [float('inf')] * n
            stack = []
            for i in range(day, n):
                if i == 0:
                    new_dp[0] = jobDifficulty[0]
                else:
                    new_dp[i] = jobDifficulty[i] + dp[i-1]
                
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    diff_incr = jobDifficulty[i] - jobDifficulty[j]
                    new_dp[i] = min(new_dp[i], new_dp[j] + diff_incr)
                
                if stack:
                    new_dp[i] = min(new_dp[i], new_dp[stack[-1]])
                stack.append(i)
            
            dp = new_dp
        
        return dp[-1]