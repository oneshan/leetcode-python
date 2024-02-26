# 0347 - Top K Frequent Elements
# Date: 2022-11-01
# Runtime: 290 ms, Memory: 18.7 MB
# Submission Id: 834639383


from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]