# 1014 - K Closest Points to Origin
# Date: 2022-11-01
# Runtime: 1837 ms, Memory: 20.4 MB
# Submission Id: 834653426


import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return point[0] ** 2 + point[1] ** 2
        
        max_heap = []
        for point in points:
            heapq.heappush(max_heap, (-dist(point), point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [point for _, point in max_heap]