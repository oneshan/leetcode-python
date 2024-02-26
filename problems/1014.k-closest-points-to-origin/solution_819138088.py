# 1014 - K Closest Points to Origin
# Date: 2022-10-10
# Runtime: 1682 ms, Memory: 20.4 MB
# Submission Id: 819138088


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2+ p[1]**2)
        return points[:k]