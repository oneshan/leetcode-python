# 0678 - Valid Parenthesis String
# Date: 2024-04-07
# Runtime: 38 ms, Memory: 16.7 MB
# Submission Id: 1225304810


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
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