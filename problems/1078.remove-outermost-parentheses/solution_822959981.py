# 1078 - Remove Outermost Parentheses
# Date: 2022-10-15
# Runtime: 97 ms, Memory: 14 MB
# Submission Id: 822959981


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ''
        count = 0
        for ch in s:  
            if ch == '(':
                stack.append('(')
                count += 1
                if count != 1: ans += ch
            else:
                stack.pop()
                count -= 1
                if count != 0: ans += ch
        return ans