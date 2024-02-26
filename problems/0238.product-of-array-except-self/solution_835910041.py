# 0238 - Product of Array Except Self
# Date: 2022-11-03
# Runtime: 362 ms, Memory: 22.4 MB
# Submission Id: 835910041


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]            
            right[n-i-1] = right[n-i] * nums[n-i]
            
        return [left[i] * right[i] for i in range(n)]