# 0238 - Product of Array Except Self
# Date: 2024-03-04
# Runtime: 165 ms, Memory: 23.9 MB
# Submission Id: 1193269580


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left_product = 1
        for i in range(n):
            ans[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans