# 1078 - Remove Outermost Parentheses
# Date: 2024-05-24
# Runtime: 38 ms, Memory: 16.6 MB
# Submission Id: 1266713673


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        left = 0
        for ch in s:
            if ch == '(':
                if left:
                    ans.append('(')
                left += 1
            else:
                left -= 1
                if left:
                    ans.append(')')
        return ''.join(ans)