# 0347 - Top K Frequent Elements
# Date: 2023-09-16
# Runtime: 102 ms, Memory: 20.8 MB
# Submission Id: 1051049491


from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        min_heap = []
        for num, count in counter.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for _, num in min_heap]