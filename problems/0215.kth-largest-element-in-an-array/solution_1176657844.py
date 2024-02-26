# 0215 - Kth Largest Element in an Array
# Date: 2024-02-16
# Runtime: 513 ms, Memory: 28.8 MB
# Submission Id: 1176657844


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        for _ in range(n-k):
            heapq.heappop(nums)
        return nums[0]