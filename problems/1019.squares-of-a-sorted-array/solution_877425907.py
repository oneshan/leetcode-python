# 1019 - Squares of a Sorted Array
# Date: 2023-01-13
# Runtime: 224 ms, Memory: 15.7 MB
# Submission Id: 877425907


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]
            
        ans = [0] * n
        i, j = 0, n-1
        for idx in range(n-1, -1, -1):
            if nums[i] >= nums[j]:
                ans[idx] = nums[i]
                i += 1
            else:
                ans[idx] = nums[j]
                j -= 1
        return ans