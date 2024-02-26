# 1988 - Minimize Maximum Pair Sum in Array
# Date: 2023-11-17
# Runtime: 975 ms, Memory: 30.9 MB
# Submission Id: 1100738218


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        
        ans = 0
        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1
        return ans