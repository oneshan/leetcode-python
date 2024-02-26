# 0504 - Base 7
# Date: 2024-02-07
# Runtime: 26 ms, Memory: 16.5 MB
# Submission Id: 1168555369


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        is_neg = False
        if num < 0:
            is_neg = True
            num *= -1

        ans = []
        while num:
            num, digit = divmod(num, 7)
            ans.append(str(digit))
            
        if is_neg:
            ans.append('-')
        return ''.join(ans[::-1])