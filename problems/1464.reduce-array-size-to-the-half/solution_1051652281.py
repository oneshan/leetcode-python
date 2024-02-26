# 1464 - Reduce Array Size to The Half
# Date: 2023-09-17
# Runtime: 511 ms, Memory: 33.7 MB
# Submission Id: 1051652281


from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        
        target = n // 2
        ans = 0
        max_heap = []
        for num, freq in counter.items():
            heapq.heappush(max_heap, -freq)
        
        while target > 0:
            freq = heapq.heappop(max_heap)
            target += freq
            ans += 1
        return ans