# 1954 - Replace All Digits with Characters
# Date: 2024-04-30
# Runtime: 28 ms, Memory: 16.5 MB
# Submission Id: 1245879817


class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(1, n, 2):
            s[i] = chr(ord(s[i-1]) + int(s[i]))
        return ''.join(s)