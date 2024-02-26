# 1078 - Remove Outermost Parentheses
# Date: 2023-10-21
# Runtime: 33 ms, Memory: 16.3 MB
# Submission Id: 1080297981


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, count = [], 0
        for ch in s:  
            if ch == '(':
                count += 1
                if count != 1:
                    ans.append(ch)
            else:
                count -= 1
                if count != 0:
                    ans.append(ch)
        return ''.join(ans)