# 1585 - The kth Factor of n
# Date: 2024-04-03
# Runtime: 24 ms, Memory: 16.5 MB
# Submission Id: 1222465876


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        heap = []

        def push(i):
            heapq.heappush(heap, -i)
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(1, isqrt(n)+1):
            if n % i == 0:
                push(i)
                if n // i != i:
                    push(n//i)
                    
        return -heap[0] if len(heap) == k else -1