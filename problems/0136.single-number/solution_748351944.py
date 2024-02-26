# 0136 - Single Number
# Date: 2022-07-16
# Runtime: 201 ms, Memory: 16.7 MB
# Submission Id: 748351944


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans