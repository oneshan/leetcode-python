# 1888 - Find Nearest Point That Has the Same X or Y Coordinate
# Date: 2022-05-30
# Runtime: 1363 ms, Memory: 19.3 MB
# Submission Id: 710484745


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_v, ans = float('inf'), -1
        for idx, point in enumerate(points):
            if point[0] == x and min_v > abs(point[1]-y):
                min_v = abs(point[1]-y)
            elif point[1] == y and min_v > abs(point[0]-x):
                min_v = abs(point[0]-x)
            else:
                continue
            ans = idx
        return ans