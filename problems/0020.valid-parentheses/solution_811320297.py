# 0020 - Valid Parentheses
# Date: 2022-09-29
# Runtime: 52 ms, Memory: 13.9 MB
# Submission Id: 811320297


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
            elif not stack:
                return False
            else:
                last = stack.pop()
                if pairs[ch] != last:
                    return False
        return len(stack) == 0
                    