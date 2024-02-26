# 1457 - Minimum Difficulty of a Job Schedule
# Date: 2023-12-29
# Runtime: 76 ms, Memory: 17.5 MB
# Submission Id: 1131304700


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        prev = [float('inf')] * n
        curr = [float('inf')] * n

        for day in range(d):
            stack = []
            for i in range(day, n):
                if i == 0:
                    curr[0] = jobDifficulty[0]
                else:
                    curr[i] = jobDifficulty[i] + prev[i-1]
                
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    diff_incr = jobDifficulty[i] - jobDifficulty[j]
                    curr[i] = min(curr[i], curr[j] + diff_incr)
                
                if stack:
                    curr[i] = min(curr[i], curr[stack[-1]])
                stack.append(i)
            
            prev, curr = curr, prev
        
        return prev[-1]