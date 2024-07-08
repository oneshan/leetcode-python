# 2221 - Check if a Parentheses String Can Be Valid
# Date: 2024-05-24
# Runtime: 141 ms, Memory: 17.8 MB
# Submission Id: 1266730576


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False

        left = right = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                left += 1
            else:
                right += 1

            if left < right:
                return False

        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                right += 1
            else:
                left += 1

            if left > right:
                return False

        return True