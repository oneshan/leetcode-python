# 0874 - Backspace String Compare
# Date: 2023-09-04
# Runtime: 35 ms, Memory: 16.1 MB
# Submission Id: 1039999176


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        for ch in s:
            if ch != '#':
                stack_s.append(ch)
            elif stack_s:
                stack_s.pop()
                
        for ch in t:
            if ch != '#':
                stack_t.append(ch)
            elif stack_t:
                stack_t.pop()
                
        return stack_s == stack_t