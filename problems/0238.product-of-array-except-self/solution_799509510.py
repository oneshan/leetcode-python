# 0238 - Product of Array Except Self
# Date: 2022-09-14
# Runtime: 270 ms, Memory: 22.4 MB
# Submission Id: 799509510


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]            
            right[-i-1] = nums[-i] * right[-i]
            
        return [left[i] * right[i] for i in range(n)]