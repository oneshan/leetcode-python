# 1950 - Sign of the Product of an Array
# Date: 2022-05-30
# Runtime: 90 ms, Memory: 13.9 MB
# Submission Id: 710487868


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_flag = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg_flag ^= 1
        return -1 if neg_flag else 1