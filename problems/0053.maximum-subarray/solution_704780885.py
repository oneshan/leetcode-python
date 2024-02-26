# 0053 - Maximum Subarray
# Date: 2022-05-22
# Runtime: 1353 ms, Memory: 27.9 MB
# Submission Id: 704780885


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum + num, num)
            ans = max(ans, current_sum)
        return ans