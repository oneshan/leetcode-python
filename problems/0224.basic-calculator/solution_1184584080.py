# 0224 - Basic Calculator
# Date: 2024-02-24
# Runtime: 59 ms, Memory: 18.4 MB
# Submission Id: 1184584080


class Solution:
    def calculate(self, s: str) -> int:
        num = ''
        ans = [[]]
        for ch in s[::-1]:

            if ch == ' ':
                continue
            if ch in '0123456789':
                num = ch + num
                continue

            if num:
                ans[-1].append(int(num))
                num = ''

            if ch == '-':
                ans[-1][-1] *= -1
            elif ch == ')':
                ans.append([])
            elif ch == '(':
                val = sum(ans.pop())
                ans[-1].append(val)

        if num:
            ans[-1].append(int(num))

        return sum(ans[-1])