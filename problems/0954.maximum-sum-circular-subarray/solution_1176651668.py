# 0954 - Maximum Sum Circular Subarray
# Date: 2024-02-16
# Runtime: 368 ms, Memory: 21.8 MB
# Submission Id: 1176651668


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        curr_min = curr_max = 0
        min_so_far, max_so_far = float('inf'), float('-inf')
        for num in nums:
            curr_max = max(curr_max+num, num)
            curr_min = min(curr_min+num, num)
            max_so_far = max(max_so_far, curr_max)
            min_so_far = min(min_so_far, curr_min)

        if min_so_far == total:
            return max_so_far
        return max(max_so_far, total - min_so_far)