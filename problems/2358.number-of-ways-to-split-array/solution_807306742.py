# 2358 - Number of Ways to Split Array
# Date: 2022-09-24
# Runtime: 2484 ms, Memory: 29.2 MB
# Submission Id: 807306742


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[-1] - nums[i]:
                ans += 1
        return ans