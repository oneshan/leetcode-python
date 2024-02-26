# 0053 - Maximum Subarray
# Date: 2024-02-16
# Runtime: 560 ms, Memory: 30.9 MB
# Submission Id: 1176646261


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, curr = float('-inf'), 0
        for num in nums:
            curr = max(curr+num, num)
            ans = max(ans, curr)
        return ans