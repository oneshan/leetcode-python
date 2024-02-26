# 0020 - Valid Parentheses
# Date: 2022-05-03
# Runtime: 71 ms, Memory: 13.9 MB
# Submission Id: 692381837


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif not stack:
                return False
            else:
                pre = stack.pop()
                if ch != pairs[pre]:
                    return False
        return len(stack) == 0