# 0136 - Single Number
# Date: 2022-10-08
# Runtime: 264 ms, Memory: 16.8 MB
# Submission Id: 817340205


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans