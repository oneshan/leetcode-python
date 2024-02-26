# 0227 - Basic Calculator II
# Date: 2024-02-25
# Runtime: 100 ms, Memory: 19.9 MB
# Submission Id: 1185004009


class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        n = len(s)

        curr, op = 0, '+'
        for idx, ch in enumerate(s):
            if ch in '0123456789':
                curr = curr * 10 + int(ch)
            if idx == n-1 or ch in {'+', '-', '*', '/'}:
                if op == '+': 
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '/':
                    stack[-1] = int(stack[-1] / curr)
                elif op == '*':
                    stack[-1] *= curr
                curr, op = 0, ch

        return sum(stack)