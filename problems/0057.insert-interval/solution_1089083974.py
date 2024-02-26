# 0057 - Insert Interval
# Date: 2023-11-01
# Runtime: 87 ms, Memory: 19.8 MB
# Submission Id: 1089083974


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx, n = 0, len(intervals)
        ans = []
        
        left, right = 0, len(intervals)-1
        while left <= right and intervals[left][1] < newInterval[0]:
            left += 1
        while left <= right and intervals[right][0] > newInterval[1]:
            right -= 1
        
        if left <= right:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right][1])
        
        return intervals[:left] + [newInterval] + intervals[right+1:]