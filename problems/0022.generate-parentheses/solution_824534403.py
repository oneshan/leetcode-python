# 0022 - Generate Parentheses
# Date: 2022-10-18
# Runtime: 65 ms, Memory: 14.3 MB
# Submission Id: 824534403


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recur(pattern, left, right):
            if len(pattern) == n * 2:
                ans.append(pattern)
            if left < n:
                recur(pattern+'(', left+1, right)
            if right < left:
                recur(pattern+')', left, right+1)
        
        recur('', 0, 0)
        return ans