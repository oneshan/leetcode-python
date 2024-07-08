# 0678 - Valid Parenthesis String
# Date: 2024-05-23
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1265744266


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        star, stack = [], []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == '*':
                star.append(idx)
            elif ch == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while stack and star:
            if stack.pop() > star.pop():
                return False

        return not stack