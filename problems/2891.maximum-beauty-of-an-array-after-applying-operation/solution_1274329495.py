# 2891 - Maximum Beauty of an Array After Applying Operation
# Date: 2024-06-01
# Runtime: 773 ms, Memory: 30.5 MB
# Submission Id: 1274329495


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        for right, num in enumerate(nums):
            if num > nums[left] + 2 * k:
                left += 1
        return right - left + 1