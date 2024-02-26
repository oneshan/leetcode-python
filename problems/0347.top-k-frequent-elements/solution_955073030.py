# 0347 - Top K Frequent Elements
# Date: 2023-05-22
# Runtime: 105 ms, Memory: 21.3 MB
# Submission Id: 955073030


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