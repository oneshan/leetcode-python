# 0678 - Valid Parenthesis String
# Date: 2024-05-23
# Runtime: 32 ms, Memory: 16.5 MB
# Submission Id: 1265748978


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        cnt_open = cnt_close = 0
        for i in range(n):
            if s[i] == '(' or s[i] == '*':
                cnt_open += 1
            else:
                cnt_open -= 1

            if cnt_open < 0:
                return False

        for i in range(n-1, -1, -1):
            if s[i] == ')' or s[i] == '*':
                cnt_close += 1
            else:
                cnt_close -= 1

            if cnt_close < 0:
                return False

        return True