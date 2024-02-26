# 0057 - Insert Interval
# Date: 2024-02-20
# Runtime: 66 ms, Memory: 20 MB
# Submission Id: 1180521470


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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