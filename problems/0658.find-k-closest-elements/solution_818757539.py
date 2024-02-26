# 0658 - Find K Closest Elements
# Date: 2022-10-10
# Runtime: 1011 ms, Memory: 16.2 MB
# Submission Id: 818757539


import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for idx, num in enumerate(arr):
            heapq.heappush(heap, (abs(num-x), num))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return sorted(ans)