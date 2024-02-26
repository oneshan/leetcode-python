# 1950 - Sign of the Product of an Array
# Date: 2022-11-12
# Runtime: 147 ms, Memory: 13.9 MB
# Submission Id: 841706652


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg += 1
        return -1 if neg & 1 else 1