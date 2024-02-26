# 0150 - Evaluate Reverse Polish Notation
# Date: 2022-07-22
# Runtime: 131 ms, Memory: 14.3 MB
# Submission Id: 753831486


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-/*':
                stack.append(int(token))
                continue
                
            n2 = stack.pop()
            n1 = stack.pop()

            if token == '+':
                stack.append(n1+n2)
            elif token == '-':
                stack.append(n1-n2)
            elif token == '*':
                stack.append(n1*n2)
            elif token == '/':
                stack.append(int(n1/n2))

        return stack[-1]