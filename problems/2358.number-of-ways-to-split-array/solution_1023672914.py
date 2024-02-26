# 2358 - Number of Ways to Split Array
# Date: 2023-08-17
# Runtime: 794 ms, Memory: 31.5 MB
# Submission Id: 1023672914


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        ans = 0
        for i in range(n-1):
            if nums[i] >= nums[-1] - nums[i]:
                ans += 1
        return ans