# 0020 - Valid Parentheses
# Date: 2022-09-29
# Runtime: 71 ms, Memory: 13.8 MB
# Submission Id: 811320610


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
                continue
            
            prev = stack.pop() if stack else '#'
            if pairs[ch] != prev:
                return False

        return len(stack) == 0
                    