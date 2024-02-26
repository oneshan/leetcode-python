# 0008 - String to Integer (atoi)
# Date: 2023-07-28
# Runtime: 50 ms, Memory: 16.2 MB
# Submission Id: 1006174785


class Solution:
    def myAtoi(self, s: str) -> int:
        
        n = len(s)
        sign, num = 1, 0
        
        i = 0
        # cleanup leading space
        while i < n and s[i] == ' ':
            i += 1
        
        # handle sign
        if i < n and s[i] == '+':
            sign = 1
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        
        # handle number
        while i < n and s[i] in '0123456789':
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        
        # Check overflow
        return max(-(1<<31), (min((1<<31)-1, num)))