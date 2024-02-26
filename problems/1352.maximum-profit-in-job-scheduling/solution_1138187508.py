# 1352 - Maximum Profit in Job Scheduling
# Date: 2024-01-06
# Runtime: 520 ms, Memory: 35.2 MB
# Submission Id: 1138187508


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        
        jobs = []
        for idx, (start, end, p) in enumerate(zip(startTime, endTime, profit)):
            jobs.append((start, 1, idx))
            jobs.append((end, -1, idx))
        jobs.sort()
        
        dp = [0] * n
        curr = 0
        for _, pos, idx in jobs:
            if pos == 1:
                dp[idx] = curr + profit[idx]
            else:
                curr = max(curr, dp[idx])
        return max(dp)