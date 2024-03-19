# 0452 - Minimum Number of Arrows to Burst Balloons
# Date: 2024-03-18
# Runtime: 1158 ms, Memory: 62.7 MB
# Submission Id: 1207067336


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()
        ans = n = len(points)

        end = points[0][1]
        for i in range(1, n):
            curr = points[i]
            if curr[0] <= end:
                ans -= 1
                end = min(end, curr[1])
            else:
                end = curr[1]
        return ans