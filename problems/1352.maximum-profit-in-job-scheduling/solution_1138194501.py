# 1352 - Maximum Profit in Job Scheduling
# Date: 2024-01-06
# Runtime: 717 ms, Memory: 108.9 MB
# Submission Id: 1138194501


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        
        jobs = []
        for start, end, p in zip(startTime, endTime, profit):
            jobs.append((start, end, p))
        jobs.sort()
        
        @cache
        def dp(idx):
            if idx == n:
                return 0

            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if jobs[mid][0] < jobs[idx][1]:
                    left = mid + 1
                else:
                    right = mid
            next_idx = left
            
            return max(dp(idx+1), jobs[idx][2] + dp(next_idx))
        
        return dp(0)