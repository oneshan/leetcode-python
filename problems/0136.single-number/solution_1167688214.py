# 0136 - Single Number
# Date: 2024-02-06
# Runtime: 107 ms, Memory: 19.1 MB
# Submission Id: 1167688214


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans