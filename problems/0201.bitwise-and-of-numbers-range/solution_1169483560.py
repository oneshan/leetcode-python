# 0201 - Bitwise AND of Numbers Range
# Date: 2024-02-08
# Runtime: 40 ms, Memory: 16.5 MB
# Submission Id: 1169483560


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= (right-1)
        return right