# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2023-12-29
# Runtime: 1005 ms, Memory: 18.7 MB
# Submission Id: 1131287699


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        max_diff = [0] * n
        max_diff[-1] = jobDifficulty[-1]
        for i in range(n-2, -1, -1):
            max_diff[i] = max(max_diff[i+1], jobDifficulty[i])
            
        @cache
        def dp(i, d):
            if d == 1:
                return max_diff[i]
            
            res = float('inf')
            curr_max = 0
            for j in range(i, n-d+1):
                curr_max = max(curr_max, jobDifficulty[j])
                res = min(res, curr_max + dp(j+1, d-1))
            return res
        
        return dp(0, d)