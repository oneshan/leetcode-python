# 0053 - Maximum Subarray
# Date: 2024-05-23
# Runtime: 566 ms, Memory: 30.9 MB
# Submission Id: 1265384214


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = 0
        for num in nums:
            curr = max(curr, 0) + num
            ans = max(ans, curr)
        return ans