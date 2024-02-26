# 1352 - Maximum Profit in Job Scheduling
# Date: 2024-01-06
# Runtime: 527 ms, Memory: 32.7 MB
# Submission Id: 1138201849


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        
        jobs = []
        for start, end, p in zip(startTime, endTime, profit):
            jobs.append((start, end, p))
        jobs.sort()
        
        max_profit = 0
        heap = []
        
        for start, end, p in jobs:
            while heap and start >= heap[0][0]:
                _, profit = heapq.heappop(heap)
                max_profit = max(max_profit, profit)
            
            heappush(heap, (end, max_profit + p))
        
        for _, profit in heap:
            max_profit = max(max_profit, profit)
        return max_profit