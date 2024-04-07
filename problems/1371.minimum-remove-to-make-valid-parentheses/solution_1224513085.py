# 1371 - Minimum Remove to Make Valid Parentheses
# Date: 2024-04-06
# Runtime: 69 ms, Memory: 18.1 MB
# Submission Id: 1224513085


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ''

        s = list(s)
        stack = []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    s[idx] = ''
        
        for idx in stack:
            s[idx] = ''
        
        return ''.join(s)