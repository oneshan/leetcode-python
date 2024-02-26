# 2358 - Number of Ways to Split Array
# Date: 2022-09-24
# Runtime: 2366 ms, Memory: 29.3 MB
# Submission Id: 807308639


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
            
        ans = left_sum = 0
        for i in range(len(nums)-1):
            left_sum += nums[i]
            if left_sum >= total - left_sum:
                ans += 1
        return ans