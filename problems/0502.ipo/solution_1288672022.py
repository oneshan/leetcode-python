# 0502 - IPO
# Date: 2024-06-15
# Runtime: 687 ms, Memory: 41.2 MB
# Submission Id: 1288672022


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)

        arr = [(c, p) for c, p in zip(capital, profits)]
        arr.sort()
        max_heap = []

        i = 0
        for _ in range(k):
            while i < n and arr[i][0] <= w:
                heapq.heappush(max_heap, -arr[i][1])
                i += 1
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)

        return w