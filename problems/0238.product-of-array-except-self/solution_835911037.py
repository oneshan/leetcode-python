# 0238 - Product of Array Except Self
# Date: 2022-11-03
# Runtime: 678 ms, Memory: 21.3 MB
# Submission Id: 835911037


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]   
         
        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
            
        return ans