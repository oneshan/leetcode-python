# 0053 - Maximum Subarray
# Date: 2022-10-18
# Runtime: 1015 ms, Memory: 27.9 MB
# Submission Id: 825141398


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            ans = max(ans, curr)
        return ans