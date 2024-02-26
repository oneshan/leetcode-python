# 0405 - Convert a Number to Hexadecimal
# Date: 2022-09-16
# Runtime: 64 ms, Memory: 14 MB
# Submission Id: 801340422


class Solution:
    def toHex(self, num: int) -> str:
        hex_string = "0123456789abcdef"
        if num == 0:
            return "0"
        if num < 0:
            num = num + ((1 << 32) - 1) + 1
        ans = []
        while num:
            num, digit = divmod(num, 16)
            ans.append(hex_string[digit])
        return ''.join(ans[::-1])