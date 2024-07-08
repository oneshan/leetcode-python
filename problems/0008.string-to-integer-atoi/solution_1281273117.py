# 0008 - String to Integer (atoi)
# Date: 2024-06-08
# Runtime: 34 ms, Memory: 16.5 MB
# Submission Id: 1281273117


class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        is_neg = False

        INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31

        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            if s[i] == ' ':
                i += 1

        if i < n and s[i] in {'+', '-'}:
            is_neg = s[i] == '-'
            i += 1

        threshold = divmod(2**31-1, 10)
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if (
                num > threshold[0] or 
                num == threshold[0] and digit > threshold[1]
            ):
                return INT_MIN if is_neg else INT_MAX
            num = num * 10 + digit
            i += 1

        return num * (-1 if is_neg else 1)