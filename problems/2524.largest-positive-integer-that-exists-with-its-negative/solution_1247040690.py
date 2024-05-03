# 2524 - Largest Positive Integer That Exists With Its Negative
# Date: 2024-05-02
# Runtime: 108 ms, Memory: 16.8 MB
# Submission Id: 1247040690


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nset = set(nums)
        ans = -1
        for num in nums:
            if num > ans and -num in nset:
                ans = num
        return ans