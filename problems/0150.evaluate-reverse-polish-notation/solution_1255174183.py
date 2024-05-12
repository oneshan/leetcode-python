# 0150 - Evaluate Reverse Polish Notation
# Date: 2024-05-11
# Runtime: 120 ms, Memory: 17.1 MB
# Submission Id: 1255174183


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calculate(a, b, operator):
            return int(eval(f'{a}{operator}{b}'))

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b, a = stack.pop(), stack.pop()
                stack.append(calculate(a, b, token))
            else:
                stack.append(int(token))
        return stack[-1]