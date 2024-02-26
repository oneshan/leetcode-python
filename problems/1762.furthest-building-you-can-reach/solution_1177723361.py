# 1762 - Furthest Building You Can Reach
# Date: 2024-02-17
# Runtime: 419 ms, Memory: 30.9 MB
# Submission Id: 1177723361


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        min_heap = []
        for i in range(n-1):
            delta = heights[i+1] - heights[i]
            if delta <= 0:
                continue
            heapq.heappush(min_heap, delta)
            if len(min_heap) <= ladders:
                continue
            bricks -= heapq.heappop(min_heap)
            if bricks < 0:
                return i
        return n - 1