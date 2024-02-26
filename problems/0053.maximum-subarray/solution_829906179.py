# 0053 - Maximum Subarray
# Date: 2022-10-25
# Runtime: 1975 ms, Memory: 28.4 MB
# Submission Id: 829906179


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = curr = float('-inf')
        for num in nums:
            curr = max(curr+num, num)
            ans = max(ans, curr)
        return ans