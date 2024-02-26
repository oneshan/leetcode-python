# 0020 - Valid Parentheses
# Date: 2022-11-03
# Runtime: 67 ms, Memory: 13.9 MB
# Submission Id: 835912445


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for ch in s:
            if ch in ')]}':
                if not stack: return False
                if pairs[stack[-1]] != ch: return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0