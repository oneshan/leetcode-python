# 3055 - Maximum Odd Binary Number
# Date: 2024-03-01
# Runtime: 48 ms, Memory: 16.5 MB
# Submission Id: 1190195520


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ans = ['0'] * n

        left = 0
        for ch in s:
            if ch == '1':
                ans[left] = '1'
                left += 1
        ans[left-1], ans[-1] = ans[-1], ans[left-1]
        return ''.join(ans)            