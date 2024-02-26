# 0761 - Employee Free Time
# Date: 2023-10-28
# Runtime: 77 ms, Memory: 18.1 MB
# Submission Id: 1085884997


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        for s in schedule:
            for interval in s:
                heapq.heappush(heap, [interval.start, interval.end])
        merged = [heapq.heappop(heap)]
        while heap:
            start, end = heapq.heappop(heap)
            if merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        ans = []
        for i in range(len(merged)-1):
            ans.append(Interval(merged[i][1], merged[i+1][0]))
        return ans