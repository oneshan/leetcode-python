# 0012 - Integer to Roman
# Date: 2022-10-16
# Runtime: 79 ms, Memory: 13.9 MB
# Submission Id: 823707540


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        ans = []
        for i, roman in zip(integer, roman):
            k, num = divmod(num, i)
            ans.append(k*roman)
            if num == 0:
                break
        return ''.join(ans)