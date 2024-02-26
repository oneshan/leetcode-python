# 2551 - Apply Operations to an Array
# Date: 2022-11-12
# Runtime: 148 ms, Memory: 14.2 MB
# Submission Id: 841742310


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1], nums[i] = nums[i-1] * 2, 0

        # move all zeros to end
        left = 0
        for right, num in enumerate(nums):
            if num:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums