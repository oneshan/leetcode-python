# 0802 - K-th Smallest Prime Fraction
# Date: 2024-05-10
# Runtime: 1223 ms, Memory: 70.1 MB
# Submission Id: 1254181452


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        max_heap = []

        for j in range(n-1, 0, -1):
            if max_heap and max_heap[0][0] > -arr[0] / arr[j]:
                break
            for i in range(j):
                heapq.heappush(max_heap, (-arr[i] / arr[j], arr[i], arr[j]))
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
                
        return [max_heap[0][1], max_heap[0][2]]