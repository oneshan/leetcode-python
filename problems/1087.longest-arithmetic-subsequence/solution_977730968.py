# 1087 - Longest Arithmetic Subsequence
# Date: 2023-06-23
# Runtime: 3067 ms, Memory: 60.6 MB
# Submission Id: 977730968


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for right in range(len(nums)):
            for left in range(right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1
        return max(dp.values())