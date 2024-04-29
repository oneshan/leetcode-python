# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2024-04-18
# Runtime: 502 ms, Memory: 17.8 MB
# Submission Id: 1235488424


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        remains = [0] * n
        curr_max = 0
        for i in range(n-1, -1, -1):
            curr_max = max(curr_max, jobDifficulty[i])
            remains[i] = curr_max
        
        @cache
        def dp(i, day):
            if day == d:
                return remains[i]
            
            res = float('inf')
            curr_max = 0
            for j in range(i, n-d+day):
                curr_max = max(curr_max, jobDifficulty[j])
                res = min(res, curr_max + dp(j+1, day+1))
            return res
                
        return dp(0, 1)