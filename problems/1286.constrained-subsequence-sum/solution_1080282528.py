# 1286 - Constrained Subsequence Sum
# Date: 2023-10-21
# Runtime: 1673 ms, Memory: 36.6 MB
# Submission Id: 1080282528


import heapq

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, curr = nums[0], 0
        heap = [(-nums[0], 0)]
        for i in range(1, n):
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))
        return ans