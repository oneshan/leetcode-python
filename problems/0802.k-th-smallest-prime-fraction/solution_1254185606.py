# 0802 - K-th Smallest Prime Fraction
# Date: 2024-05-10
# Runtime: 564 ms, Memory: 16.8 MB
# Submission Id: 1254185606


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        for j in range(1, n):
            heapq.heappush(min_heap, (arr[0] / arr[j], 0, j))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if i + 1 < j:
                heapq.heappush(min_heap, (arr[i+1] / arr[j], i+1, j))
        
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]