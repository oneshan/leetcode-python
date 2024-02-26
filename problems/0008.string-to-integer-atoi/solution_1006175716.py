# 0008 - String to Integer (atoi)
# Date: 2023-07-28
# Runtime: 41 ms, Memory: 16.2 MB
# Submission Id: 1006175716


class Solution:
    def myAtoi(self, s: str) -> int:
        
        n = len(s)
        idx = 0

        # cleanup leading space
        while idx < n and s[idx] == ' ':
            idx += 1
        
        # handle sign
        sign = 1
        if idx < n and s[idx] == '+':
            sign = 1
            idx += 1
        elif idx < n and s[idx] == '-':
            sign = -1
            idx += 1
        
        # handle number
        num = 0
        while idx < n and s[idx] in '0123456789':
            num = num * 10 + int(s[idx])
            idx += 1
        num *= sign
        
        # Check overflow
        return max(-(1<<31), (min((1<<31)-1, num)))