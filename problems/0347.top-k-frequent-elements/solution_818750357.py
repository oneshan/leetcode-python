# 0347 - Top K Frequent Elements
# Date: 2022-10-10
# Runtime: 103 ms, Memory: 18.8 MB
# Submission Id: 818750357


from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []
        
        for num in nums:
            freq[num] += 1
        
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]