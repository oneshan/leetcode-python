# 0238 - Product of Array Except Self
# Date: 2022-09-14
# Runtime: 551 ms, Memory: 21.3 MB
# Submission Id: 799510384


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [1] * n
        for i in range(1, n):
            ans[i] = nums[i-1] * ans[i-1]
        
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
            
        return ans