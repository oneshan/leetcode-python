# 0224 - Basic Calculator
# Date: 2024-02-25
# Runtime: 63 ms, Memory: 17.9 MB
# Submission Id: 1184990463


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        curr, sign = 0, 1
        for ch in s:
            if ch == ' ':
                continue
            if ch in '0123456789':
                curr = curr * 10 + int(ch)
            elif ch == '(':
                stack.append((res, sign))
                res, sign = 0, 1
            elif ch == ')':
                res += sign * curr
                prev_num, prev_sign = stack.pop()
                res *= prev_sign
                res += prev_num
                curr = 0
            elif ch == '-':
                res += sign * curr
                curr, sign = 0, -1
            elif ch == '+':
                res += sign * curr
                curr, sign = 0, 1
        
        return res + sign * curr