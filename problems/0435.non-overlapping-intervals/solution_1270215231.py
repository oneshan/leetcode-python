# 0435 - Non-overlapping Intervals
# Date: 2024-05-28
# Runtime: 1218 ms, Memory: 55 MB
# Submission Id: 1270215231


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prev_end = float('-inf')
        for start, end in intervals:
            # no overlap
            if start >= prev_end:
                prev_end = end
            # overlap
            else:
                ans += 1
                prev_end =  min(prev_end, end)
        return ans