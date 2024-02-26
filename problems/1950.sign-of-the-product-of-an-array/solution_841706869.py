# 1950 - Sign of the Product of an Array
# Date: 2022-11-12
# Runtime: 151 ms, Memory: 14 MB
# Submission Id: 841706869


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg ^= 1
        return -1 if neg else 1