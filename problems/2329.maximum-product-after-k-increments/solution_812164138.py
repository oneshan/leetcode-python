# 2329 - Maximum Product After K Increments
# Date: 2022-10-01
# Runtime: 3728 ms, Memory: 24.5 MB
# Submission Id: 812164138


import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            min_val = heapq.heappop(nums)
            heapq.heappush(nums, min_val+1)
        ans = 1
        for num in nums:
            ans *= num
            ans %= (10**9+7)
        return ans