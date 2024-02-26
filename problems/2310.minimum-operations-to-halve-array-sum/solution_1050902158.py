# 2310 - Minimum Operations to Halve Array Sum
# Date: 2023-09-16
# Runtime: 879 ms, Memory: 31.1 MB
# Submission Id: 1050902158


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