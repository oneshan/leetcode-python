# 2329 - Maximum Product After K Increments
# Date: 2023-09-24
# Runtime: 1191 ms, Memory: 27 MB
# Submission Id: 1057868239


import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        heapq.heapify(nums)
        for _ in range(k):
            num = heapq.heappop(nums)
            heapq.heappush(nums, num+1)
            
        ans = 1
        for num in nums:
            ans = (ans * num) % 1_000_000_007
        return ans