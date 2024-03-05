# 1371 - Minimum Remove to Make Valid Parentheses
# Date: 2024-03-04
# Runtime: 79 ms, Memory: 18.6 MB
# Submission Id: 1193168869


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ''

        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')' and right < left:
                right += 1

        validate_pairs = min(left, right)
        
        left = right = 0
        ans = []
        for ch in s:
            if ch == '(':
                if left < validate_pairs:
                    ans.append('(')
                    left += 1
            elif ch == ')':
                if right < validate_pairs and right < left:
                    ans.append(')')
                    right += 1
            else:
                ans.append(ch)
        return ''.join(ans)