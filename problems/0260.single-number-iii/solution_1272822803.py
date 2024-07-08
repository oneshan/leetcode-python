# 0260 - Single Number III
# Date: 2024-05-31
# Runtime: 63 ms, Memory: 18.5 MB
# Submission Id: 1272822803


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # ones = a ^ b
        ones = 0
        for num in nums:
            ones ^= num

        # rightmost 1-bit
        diff = ones & (~ones + 1)

        a = 0
        for num in nums:
            if num & diff:
                a ^= num
        
        return [a, ones ^ a]