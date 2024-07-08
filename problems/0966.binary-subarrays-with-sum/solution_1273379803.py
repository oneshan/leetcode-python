# 0966 - Binary Subarrays With Sum
# Date: 2024-05-31
# Runtime: 226 ms, Memory: 17.2 MB
# Submission Id: 1273379803


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def at_most(target):
            res = left = curr = 0        
            for right, num in enumerate(nums):
                curr += num
                while left <= right and curr > target:
                    curr -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        return at_most(goal) - at_most(goal-1)