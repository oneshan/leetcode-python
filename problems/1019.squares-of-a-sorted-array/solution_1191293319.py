# 1019 - Squares of a Sorted Array
# Date: 2024-03-02
# Runtime: 153 ms, Memory: 18.8 MB
# Submission Id: 1191293319


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        left, right = 0, n-1

        idx = n-1
        while idx >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                ans[idx] = nums[left] * nums[left]
                left += 1
            else:
                ans[idx] = nums[right] * nums[right]
                right -= 1
            idx -= 1
        return ans