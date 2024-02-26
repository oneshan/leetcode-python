# 2310 - Minimum Operations to Halve Array Sum
# Date: 2022-10-09
# Runtime: 2254 ms, Memory: 28.9 MB
# Submission Id: 818594606


import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        
        # Build max-heap: O(N)
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        ans = reduce_sum = 0
        while nums:
            val = heapq.heappop(nums) / 2
            ans += 1
            reduce_sum -= val
            if reduce_sum >= total / 2:
                return ans
            heapq.heappush(nums, val)