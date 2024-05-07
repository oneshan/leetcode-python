# 0347 - Top K Frequent Elements
# Date: 2024-05-06
# Runtime: 80 ms, Memory: 21.2 MB
# Submission Id: 1250811327


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]