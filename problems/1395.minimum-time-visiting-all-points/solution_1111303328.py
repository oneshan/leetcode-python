# 1395 - Minimum Time Visiting All Points
# Date: 2023-12-03
# Runtime: 61 ms, Memory: 16.4 MB
# Submission Id: 1111303328


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        
        for i in range(n-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            ans += max(abs(y1-y2), abs(x1-x2))
        return ans