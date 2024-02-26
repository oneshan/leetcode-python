# 2310 - Minimum Operations to Halve Array Sum
# Date: 2022-10-09
# Runtime: 2548 ms, Memory: 28.8 MB
# Submission Id: 818597017


import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        
        # Build max-heap: O(N)
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        ans = 0
        while target > 0:
            ans += 1
            val = heapq.heappop(heap) / 2
            target += val
            heapq.heappush(heap, val)
        return ans