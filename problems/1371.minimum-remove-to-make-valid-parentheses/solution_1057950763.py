# 1371 - Minimum Remove to Make Valid Parentheses
# Date: 2023-09-24
# Runtime: 98 ms, Memory: 19.4 MB
# Submission Id: 1057950763


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # remove ')'
        chars = []
        balance = opens = 0
        for ch in s:
            if ch == '(':
                opens += 1
                balance += 1
            elif ch == ')':
                if balance == 0:
                    continue
                balance -= 1
            chars.append(ch)
        
        # remove '('
        ans = []
        opens -= balance
        for ch in chars:
            if ch == '(':
                opens -= 1
                if opens < 0:
                    continue
            ans.append(ch)

        return ''.join(ans)