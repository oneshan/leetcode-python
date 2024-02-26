# 0020 - Valid Parentheses
# Date: 2022-07-22
# Runtime: 64 ms, Memory: 14 MB
# Submission Id: 753741470


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
            if not stack:
                return False
            left = stack.pop()
            if pair[ch] != left:
                return False
        return len(stack) == 0