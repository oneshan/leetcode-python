# 0022 - Generate Parentheses
# Date: 2022-12-05
# Runtime: 69 ms, Memory: 14.2 MB
# Submission Id: 855028576


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        pattern = [''] * (n << 1)
        
        def recur(pattern, left, right):
            if left == right == n:
                ans.append(''.join(pattern))
            if left < n:
                pattern[left+right] = '('
                recur(pattern, left+1, right)
            if right < left:
                pattern[left+right] = ')'
                recur(pattern, left, right+1)
        
        recur(pattern, 0, 0)
        return ans