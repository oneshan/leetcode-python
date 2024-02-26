# 0067 - Add Binary
# Date: 2024-02-06
# Runtime: 37 ms, Memory: 16.5 MB
# Submission Id: 1167686046


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            tmp = x ^ y
            carry = (x & y) << 1
            x, y = tmp, carry
        return bin(x)[2:]