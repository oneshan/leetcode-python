# 0201 - Bitwise AND of Numbers Range
# Date: 2024-02-21
# Runtime: 49 ms, Memory: 16.6 MB
# Submission Id: 1181512639


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= (right-1)
        return right