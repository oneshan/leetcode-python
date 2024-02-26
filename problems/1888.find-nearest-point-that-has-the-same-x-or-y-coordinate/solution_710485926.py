# 1888 - Find Nearest Point That Has the Same X or Y Coordinate
# Date: 2022-05-30
# Runtime: 1319 ms, Memory: 19.3 MB
# Submission Id: 710485926


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_v, ans = float('inf'), -1
        for idx, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = abs(point[0]-x) + abs(point[1]-y)
                if dist < min_v:
                    min_v = dist
                    ans = idx
        return ans