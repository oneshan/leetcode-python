# 0012 - Integer to Roman
# Date: 2022-10-16
# Runtime: 46 ms, Memory: 13.8 MB
# Submission Id: 823710749


class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            3: ["", "M", "MM", "MMM"],
            2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        }
        
        count, ans = 0, ''
        while num:
            num, digit = divmod(num, 10)
            ans = mapping[count][digit] + ans
            count += 1
        return ans