# 0347 - Top K Frequent Elements
# Date: 2022-11-01
# Runtime: 255 ms, Memory: 18.8 MB
# Submission Id: 834639798


from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(heap)
        ans = [heapq.heappop(heap)[1] for _ in range(k)]
        return ans