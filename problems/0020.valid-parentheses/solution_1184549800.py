# 0020 - Valid Parentheses
# Date: 2024-02-24
# Runtime: 29 ms, Memory: 16.6 MB
# Submission Id: 1184549800


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif stack:
                prev = stack.pop()
                if pairs[prev] != ch:
                    return False
            else:
                return False
        return len(stack) == 0