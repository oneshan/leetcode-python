# 0075 - Sort Colors
# Date: 2024-06-12
# Runtime: 32 ms, Memory: 16.6 MB
# Submission Id: 1285553251


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            else:
                i +=1