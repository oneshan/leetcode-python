# 0347 - Top K Frequent Elements
# Date: 2022-07-19
# Runtime: 182 ms, Memory: 18.5 MB
# Submission Id: 751133479


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [freq for score, freq in heap]