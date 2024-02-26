# 1888 - Find Nearest Point That Has the Same X or Y Coordinate
# Date: 2022-11-11
# Runtime: 1872 ms, Memory: 19.2 MB
# Submission Id: 841352415


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        curr_min, curr_idx = float('inf'), -1
        for idx, point in enumerate(points):
            if point[0] != x and point[1] != y:
                continue
            dist = (point[0]-x)**2 + (point[1]-y)**2
            if dist < curr_min:
                curr_min, curr_idx = dist, idx
        return curr_idx