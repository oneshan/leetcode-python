# 0678 - Valid Parenthesis String
# Date: 2024-04-07
# Runtime: 32 ms, Memory: 16.6 MB
# Submission Id: 1225309899


class Solution:
    def checkValidString(self, s: str) -> bool:
        c_min = c_max = 0
        for ch in s:
            if ch == '(':
                c_min += 1
                c_max += 1
            elif ch == '*':
                c_min = max(0, c_min-1)
                c_max += 1
            elif ch == ')':
                c_min = max(0, c_min-1)
                c_max -= 1

            if c_max < 0:
                return False
                
        return c_min == 0