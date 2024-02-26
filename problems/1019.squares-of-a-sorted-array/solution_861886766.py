# 1019 - Squares of a Sorted Array
# Date: 2022-12-19
# Runtime: 222 ms, Memory: 16.3 MB
# Submission Id: 861886766


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)        
        ans = [0] * n
        left, right = 0, n-1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                ans[i] = nums[right] * nums[right]
                right -= 1
            else:
                ans[i] = nums[left] * nums[left]
                left += 1
        return ans