# 1737 - Maximum Nesting Depth of the Parentheses
# Date: 2024-04-04
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1222634658


class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = 0
        for ch in s:
            if ch == '(':
                stack += 1
            if ch == ')':
                stack -= 1
            ans = max(ans, stack)        
        return ans
