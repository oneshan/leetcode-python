# 0347 - Top K Frequent Elements
# Date: 2022-11-03
# Runtime: 110 ms, Memory: 18.6 MB
# Submission Id: 835907036


from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        for num in nums:
            table[num] += 1
        
        min_heap = []
        for num, count in table.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for count, num in min_heap]