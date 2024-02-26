# 0022 - Generate Parentheses
# Date: 2023-09-19
# Runtime: 51 ms, Memory: 16.6 MB
# Submission Id: 1053603768


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(arr, left, right):
            if left == right == n:
                ans.append(''.join(arr))
                return
            if left < n:
                arr.append('(')
                backtrack(arr, left+1, right)
                arr.pop()
            if right < left:
                arr.append(')')
                backtrack(arr, left, right+1)
                arr.pop()
        
        backtrack([], 0, 0)
        return ans