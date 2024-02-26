# 0435 - Non-overlapping Intervals
# Date: 2023-07-19
# Runtime: 1333 ms, Memory: 55.2 MB
# Submission Id: 998472415


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        prev_end = -inf
        
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                ans += 1
        return ans