# 0678 - Valid Parenthesis String
# Date: 2024-05-23
# Runtime: 94 ms, Memory: 30 MB
# Submission Id: 1265742214


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @cache
        def dp(i, left, right):
            if i == n:
                return left == right
            if right > left:
                return False
            
            if s[i] == '(':
                return dp(i+1, left+1, right)

            if s[i] == ')':
                return dp(i+1, left, right+1)

            if s[i] == '*':
                return dp(i+1, left, right) or dp(i+1, left+1, right) or dp(i+1, left, right+1)


        return dp(0, 0, 0)