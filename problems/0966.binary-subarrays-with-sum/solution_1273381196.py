# 0966 - Binary Subarrays With Sum
# Date: 2024-05-31
# Runtime: 202 ms, Memory: 17.3 MB
# Submission Id: 1273381196


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        ans = left = count = curr_sum = 0
        for right, num in enumerate(nums):
            if num:
                curr_sum += 1
                count = 0
            while left <= right and curr_sum >= goal:
                if curr_sum == goal:
                    count += 1
                curr_sum -= nums[left]
                left += 1

            ans += count
                
        return ans