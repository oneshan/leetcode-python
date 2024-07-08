# 0032 - Longest Valid Parentheses
# Date: 2024-05-24
# Runtime: 36 ms, Memory: 16.7 MB
# Submission Id: 1266705695


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0

        left = right = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                ans = max(ans, 2 * right)
            elif left < right:
                left = right = 0

        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * right)
            elif left > right:
                left = right = 0

        return ans