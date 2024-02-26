# 0012 - Integer to Roman
# Date: 2024-02-22
# Runtime: 48 ms, Memory: 16.4 MB
# Submission Id: 1182712441


class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        ans = []
        for i, ch in zip(integers, romans):
            k, num = divmod(num, i)
            ans.append(k*ch)
            if num == 0:
                break
        return ''.join(ans)