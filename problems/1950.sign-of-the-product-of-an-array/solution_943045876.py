# 1950 - Sign of the Product of an Array
# Date: 2023-05-02
# Runtime: 71 ms, Memory: 16.5 MB
# Submission Id: 943045876


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg ^= 1
        return -1 if neg else 1