# 0957 - Minimum Add to Make Parentheses Valid
# Date: 2024-03-17
# Runtime: 38 ms, Memory: 16.5 MB
# Submission Id: 1206284488


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        stack = []
        pairs = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif stack:
                pairs += 2
                stack.pop()
        
        return n - pairs