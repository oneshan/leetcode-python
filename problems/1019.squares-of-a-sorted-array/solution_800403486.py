# 1019 - Squares of a Sorted Array
# Date: 2022-09-15
# Runtime: 466 ms, Memory: 16.3 MB
# Submission Id: 800403486


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        
        left, right = 0, len(nums)-1

        idx = right
        while left <= right:
            n1 = nums[left] * nums[left]
            n2 = nums[right] * nums[right]
            if n1 > n2:
                ans[idx] = n1 
                left += 1
            else:
                ans[idx] = n2
                right -= 1
            idx -= 1
        return ans