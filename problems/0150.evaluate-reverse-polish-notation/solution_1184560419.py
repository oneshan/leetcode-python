# 0150 - Evaluate Reverse Polish Notation
# Date: 2024-02-24
# Runtime: 66 ms, Memory: 17.1 MB
# Submission Id: 1184560419


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a+b)
            elif token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a-b)
            elif token == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a*b)
            elif token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[-1]