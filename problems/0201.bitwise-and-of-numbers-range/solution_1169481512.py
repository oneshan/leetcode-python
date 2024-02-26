# 0201 - Bitwise AND of Numbers Range
# Date: 2024-02-08
# Runtime: 47 ms, Memory: 16.6 MB
# Submission Id: 1169481512


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bits = 0
        while left != right:
            left >>= 1
            right >>= 1
            bits += 1
        return left << bits