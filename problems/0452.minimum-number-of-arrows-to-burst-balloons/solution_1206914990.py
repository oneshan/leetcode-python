# 0452 - Minimum Number of Arrows to Burst Balloons
# Date: 2024-03-18
# Runtime: 989 ms, Memory: 62.8 MB
# Submission Id: 1206914990


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        ans = 1
        curr_end = points[0][1]
        for start, end in points:
            if start > curr_end:
                ans += 1
                curr_end = end
        return ans