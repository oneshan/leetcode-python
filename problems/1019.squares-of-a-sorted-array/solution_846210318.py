# 1019 - Squares of a Sorted Array
# Date: 2022-11-19
# Runtime: 646 ms, Memory: 15.8 MB
# Submission Id: 846210318


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]

        idx, ans = n-1, [0] * n
        left, right = 0, n-1
        while left <= right:
            if nums[left] < nums[right]:
                ans[idx] = nums[right]
                right -= 1
            else:
                ans[idx] = nums[left]
                left += 1
            idx -= 1
        return ans