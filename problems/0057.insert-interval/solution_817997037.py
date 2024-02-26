# 0057 - Insert Interval
# Date: 2022-10-09
# Runtime: 101 ms, Memory: 17.6 MB
# Submission Id: 817997037


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Find boundary
        left, right = 0, len(intervals)-1
        while left <= right and intervals[left][1] < newInterval[0]:
            left += 1
        while left <= right and intervals[right][0] > newInterval[1]:
            right -= 1
        
        # Merge
        if left <= right:
            newInterval[0] = min(intervals[left][0], newInterval[0])
            newInterval[1] = max(intervals[right][1], newInterval[1])

        return intervals[:left] + [newInterval] + intervals[right + 1:]
