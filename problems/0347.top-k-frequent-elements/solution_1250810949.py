# 0347 - Top K Frequent Elements
# Date: 2024-05-06
# Runtime: 87 ms, Memory: 21.1 MB
# Submission Id: 1250810949


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans[::-1]