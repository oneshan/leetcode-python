# 0020 - Valid Parentheses
# Date: 2022-07-22
# Runtime: 51 ms, Memory: 14 MB
# Submission Id: 753743412


class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for ch in s:
            if ch not in pair:
                stack.append(ch)
                continue
            left = stack.pop() if stack else '#'
            if pair[ch] != left:
                return False
        return len(stack) == 0