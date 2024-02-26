# 0022 - Generate Parentheses
# Date: 2022-12-06
# Runtime: 35 ms, Memory: 14.3 MB
# Submission Id: 855431779


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracking(arr, left, right):
            if left == right == n:
                ans.append(''.join(arr))
                return
            if left < n:
                arr.append('(')
                backtracking(arr, left+1, right)
                arr.pop()
            if right < left:
                arr.append(')')
                backtracking(arr, left, right+1)
                arr.pop()
        
        backtracking([], 0, 0)
        return ans