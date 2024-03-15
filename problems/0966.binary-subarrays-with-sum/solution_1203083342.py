# 0966 - Binary Subarrays With Sum
# Date: 2024-03-14
# Runtime: 231 ms, Memory: 17.3 MB
# Submission Id: 1203083342


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left = curr = prefix_zero = ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while left < right and (nums[left] == 0 or curr > goal):
                if nums[left] == 1:
                    prefix_zero = 0
                else:
                    prefix_zero += 1
                curr -= nums[left]
                left += 1
            if curr == goal:
                ans += 1 + prefix_zero
        return ans