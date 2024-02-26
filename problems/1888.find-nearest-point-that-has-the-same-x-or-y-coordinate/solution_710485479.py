# 1888 - Find Nearest Point That Has the Same X or Y Coordinate
# Date: 2022-05-30
# Runtime: 1367 ms, Memory: 19.2 MB
# Submission Id: 710485479


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_v, ans = float('inf'), -1
        for idx, point in enumerate(points):
            if point[0] == x or point[1] == y:
                x1 = abs(point[0]-x)
                y1 = abs(point[1]-y)
                if x1 + y1 < min_v:
                    min_v = x1 + y1
                    ans = idx
        return ans