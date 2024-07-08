# 0678 - Valid Parenthesis String
# Date: 2024-05-23
# Runtime: 40 ms, Memory: 17.4 MB
# Submission Id: 1265753692


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @cache
        def dp(i, cnt_open):
            if i == n:
                return cnt_open == 0
            if cnt_open < 0:
                return False
            
            if s[i] == '(':
                return dp(i+1, cnt_open+1)

            if s[i] == ')':
                return dp(i+1, cnt_open-1)

            if s[i] == '*':
                return dp(i+1, cnt_open) or dp(i+1, cnt_open+1) or dp(i+1, cnt_open-1)


        return dp(0, 0)