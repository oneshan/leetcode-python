# 1019 - Squares of a Sorted Array
# Date: 2023-08-17
# Runtime: 189 ms, Memory: 18.5 MB
# Submission Id: 1023651713


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [num * num for num in nums]
        left, right = 0, len(nums)-1
        ans = [0] * len(nums)
        
        idx = right
        while idx >= 0:
            if nums[left] >= nums[right]:
                ans[idx] = nums[left]
                left += 1
            else:
                ans[idx] = nums[right]
                right -= 1
            idx -= 1
        return ans