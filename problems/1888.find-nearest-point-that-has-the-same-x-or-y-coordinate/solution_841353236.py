# 1888 - Find Nearest Point That Has the Same X or Y Coordinate
# Date: 2022-11-11
# Runtime: 1490 ms, Memory: 19.1 MB
# Submission Id: 841353236


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        curr_min, curr_idx = float('inf'), -1
        for idx, point in enumerate(points):
            if point[0] != x and point[1] != y:
                continue
            dist = abs(point[0]-x) + abs(point[1]-y)
            if dist < curr_min:
                curr_min, curr_idx = dist, idx
        return curr_idx