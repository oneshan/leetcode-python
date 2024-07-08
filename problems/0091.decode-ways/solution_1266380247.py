# 0091 - Decode Ways
# Date: 2024-05-24
# Runtime: 39 ms, Memory: 16.4 MB
# Submission Id: 1266380247


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        p2 = p1 = 1
        prev = -1
        for ch in s:
            num = int(ch)
            count = 0
            if num > 0:
                count += p1
            if prev == 1 or (prev == 2 and num < 7):
                count += p2

            p2, p1 = p1, count
            prev = num

        return p1