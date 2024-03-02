# 0022 - Generate Parentheses
# Date: 2024-03-01
# Runtime: 29 ms, Memory: 16.8 MB
# Submission Id: 1190381508


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def recur(left, right, curr):
            if left == right == n:
                self.ans.append(''.join(curr))
                return
            if left < n:
                curr.append('(')
                recur(left+1, right, curr)
                curr.pop()

            if right < left:
                curr.append(')')
                recur(left, right+1, curr)
                curr.pop()


        recur(0, 0, [])
        return self.ans