# 2551 - Apply Operations to an Array
# Date: 2022-11-12
# Runtime: 114 ms, Memory: 14.3 MB
# Submission Id: 841741801


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1], nums[i] = nums[i-1] * 2, 0
    
        idx = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[idx] = nums[i]
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
        return nums