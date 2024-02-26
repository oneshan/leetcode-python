# 1014 - K Closest Points to Origin
# Date: 2022-10-10
# Runtime: 1113 ms, Memory: 20.2 MB
# Submission Id: 819137276


import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_arr = sorted(points, key=lambda p: p[0]**2+ p[1]**2)
        return sorted_arr[:k]