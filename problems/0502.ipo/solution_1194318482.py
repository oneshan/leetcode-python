# 0502 - IPO
# Date: 2024-03-05
# Runtime: 767 ms, Memory: 41.3 MB
# Submission Id: 1194318482


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)

        heap = [(c, -p) for p, c in zip(profits, capital)]
        heapq.heapify(heap)

        candidates = []
        for _ in range(k):
            while heap and heap[0][0] <= w:
                c, p = heapq.heappop(heap)
                heapq.heappush(candidates, p)
            if not candidates:
                break
            w -= heapq.heappop(candidates)

        return w