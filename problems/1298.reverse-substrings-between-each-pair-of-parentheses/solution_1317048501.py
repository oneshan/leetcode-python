# 1298 - Reverse Substrings Between Each Pair of Parentheses
# Date: 2024-07-11
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1317048501


class Solution:
    def reverseParentheses(self, s: str) -> str:

        pairs = {}
        stack = []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                prev = stack.pop()
                pairs[idx], pairs[prev] = prev, idx
        
        ans = []
        idx, delta = 0, 1
        while idx < len(s):
            if idx in pairs:
                idx = pairs[idx]
                delta = -delta
            else:
                ans.append(s[idx])
            idx += delta

        return ''.join(ans)