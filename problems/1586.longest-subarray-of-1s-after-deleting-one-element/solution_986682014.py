# 1586 - Longest Subarray of 1's After Deleting One Element
# Date: 2023-07-05
# Runtime: 419 ms, Memory: 18.9 MB
# Submission Id: 986682014


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = zeroes = ans = 0
        for right, num in enumerate(nums):
            zeroes += (num == 0)
            while zeroes > 1:
                zeroes -= (nums[left] == 0)
                left += 1
            ans = max(ans, right - left)
        return ans