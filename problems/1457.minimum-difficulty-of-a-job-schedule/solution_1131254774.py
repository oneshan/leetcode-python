# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2023-12-29
# Runtime: 1100 ms, Memory: 18.7 MB
# Submission Id: 1131254774


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        max_difficulty = [0] * n
        max_difficulty[-1] = jobDifficulty[-1]
        for i in range(n-2, -1, -1):
            max_difficulty[i] = max(max_difficulty[i+1], jobDifficulty[i])
        
        @cache
        def dp(i, d):
            if d == 1:
                return max_difficulty[i]
            
            res = float('inf')
            curr_max = jobDifficulty[i]
            for j in range(i, n-d+1):
                curr_max = max(curr_max, jobDifficulty[j])
                res = min(res, curr_max + dp(j+1, d-1))
            
            return res
        
        return dp(0, d)