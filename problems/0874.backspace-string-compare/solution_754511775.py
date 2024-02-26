# 0874 - Backspace String Compare
# Date: 2022-07-23
# Runtime: 37 ms, Memory: 13.9 MB
# Submission Id: 754511775


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for ch in s:
            if ch == '#':
                if stack_s: stack_s.pop()
            else:
                stack_s.append(ch)
                
        stack_t = []
        for ch in t:
            if ch == '#':
                if stack_t: stack_t.pop()
            else:
                stack_t.append(ch)
        return stack_s == stack_t