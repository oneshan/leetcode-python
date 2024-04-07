# 1371 - Minimum Remove to Make Valid Parentheses
# Date: 2024-04-06
# Runtime: 85 ms, Memory: 18.7 MB
# Submission Id: 1224511953


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ''

        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')' and left > right:
                right += 1
        valid_pairs = min(left, right)

        ans = []
        left = right = 0
        for ch in s:
            if ch == '(':
                if left == valid_pairs:
                    continue
                left += 1
            elif ch == ')':
                if left <= right:
                    continue
                right += 1
            ans.append(ch)
        return ''.join(ans)