# 0976 - Minimum Area Rectangle
# Date: 2023-10-28
# Runtime: 1492 ms, Memory: 16.7 MB
# Submission Id: 1086011652


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set(map(tuple, points))
        ans = float('inf')
        n = len(points)
        
        for i in range(n):
            p1 = points[i]
            for j in range(i):
                p2 = points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                if (p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set:
                    area = abs((p1[0]-p2[0]) * (p1[1]-p2[1]))
                    ans = min(ans, area)
        
        return ans if ans != float('inf') else 0