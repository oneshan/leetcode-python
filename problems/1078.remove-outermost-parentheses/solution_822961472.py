# 1078 - Remove Outermost Parentheses
# Date: 2022-10-15
# Runtime: 62 ms, Memory: 14 MB
# Submission Id: 822961472


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, count = [], 0
        for ch in s:  
            if ch == '(':
                count += 1
                if count != 1: ans.append(ch)
            else:
                count -= 1
                if count != 0: ans.append(ch)
        return ''.join(ans)