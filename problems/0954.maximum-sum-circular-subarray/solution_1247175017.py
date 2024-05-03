# 0954 - Maximum Sum Circular Subarray
# Date: 2024-05-02
# Runtime: 378 ms, Memory: 21.9 MB
# Submission Id: 1247175017


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        curr_min = curr_max = 0
        min_so_far, max_so_far = float('inf'), float('-inf')
        for num in nums:
            curr_max = max(curr_max+num, num)
            curr_min = min(curr_min+num, num)
            max_so_far = max(max_so_far, curr_max)
            min_so_far = min(min_so_far, curr_min)
            
        # all negative
        if min_so_far == total:
            return max_so_far
        
        return max(max_so_far, total - min_so_far)