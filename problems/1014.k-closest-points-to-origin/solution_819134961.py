# 1014 - K Closest Points to Origin
# Date: 2022-10-10
# Runtime: 864 ms, Memory: 20.3 MB
# Submission Id: 819134961


import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
            