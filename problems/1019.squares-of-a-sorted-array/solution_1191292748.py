# 1019 - Squares of a Sorted Array
# Date: 2024-03-02
# Runtime: 169 ms, Memory: 18.3 MB
# Submission Id: 1191292748


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]

        ans = [0] * n
        left, right = 0, n-1

        idx = n-1
        while idx >= 0:
            if nums[left] >= nums[right]:
                ans[idx] = nums[left]
                left += 1
            else:
                ans[idx] = nums[right]
                right -= 1
            idx -= 1
        return ans