# 2551 - Apply Operations to an Array
# Date: 2022-11-06
# Runtime: 115 ms, Memory: 14.1 MB
# Submission Id: 837979234


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
            else:
                left = right

        # move all zeros to end
        left = 0
        for right, num in enumerate(nums):
            if num:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums