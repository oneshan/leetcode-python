# 0405 - Convert a Number to Hexadecimal
# Date: 2024-02-07
# Runtime: 34 ms, Memory: 16.5 MB
# Submission Id: 1168561498


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        if num < 0:
            num = (((1 << 32) -1) ^ abs(num)) + 1
        
        hex_digit = "0123456789abcdef"
        ans = []
        while num:
            num, digit = divmod(num, 16)
            ans.append(hex_digit[digit])
        return ''.join(ans[::-1])