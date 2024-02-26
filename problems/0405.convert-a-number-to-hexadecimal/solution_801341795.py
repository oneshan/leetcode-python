# 0405 - Convert a Number to Hexadecimal
# Date: 2022-09-16
# Runtime: 68 ms, Memory: 13.8 MB
# Submission Id: 801341795


class Solution:
    def toHex(self, num: int) -> str:
        hex_string = "0123456789abcdef"
        if num == 0:
            return "0"
        if num < 0:
            num = num + ((1 << 32) - 1) + 1
        ans = ""
        while num:
            digit = num & 15
            num >>= 4
            ans = hex_string[digit] + ans
        return ans