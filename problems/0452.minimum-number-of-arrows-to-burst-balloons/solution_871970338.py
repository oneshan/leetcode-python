# 0452 - Minimum Number of Arrows to Burst Balloons
# Date: 2023-01-05
# Runtime: 1315 ms, Memory: 59.8 MB
# Submission Id: 871970338


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        ans = 1
        curr_end = points[0][1]
        for start, end in points:
            if curr_end < start:
                ans += 1
                curr_end = end
        return ans