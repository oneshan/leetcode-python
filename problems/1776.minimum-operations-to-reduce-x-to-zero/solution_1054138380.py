# 1776 - Minimum Operations to Reduce X to Zero
# Date: 2023-09-20
# Runtime: 969 ms, Memory: 30.3 MB
# Submission Id: 1054138380


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        
        left = curr_sum = 0
        ans = float('inf')
        for right in range(n):
            curr_sum += nums[right]
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                ans = min(ans, n - (right - left + 1))
        return ans if ans != float('inf') else -1