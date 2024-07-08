# 0678 - Valid Parenthesis String
# Date: 2024-05-24
# Runtime: 37 ms, Memory: 16.6 MB
# Submission Id: 1265946072


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min = open_max = 0
        for ch in s:
            if ch == '(':
                open_min, open_max = open_min + 1, open_max + 1
            elif ch == ')':
                open_min, open_max = open_min - 1, open_max - 1
            elif ch == '*':
                open_min, open_max = open_min - 1, open_max + 1

            if open_max < 0:
                return False
            if open_min < 0:
                open_min = 0

        return open_min == 0