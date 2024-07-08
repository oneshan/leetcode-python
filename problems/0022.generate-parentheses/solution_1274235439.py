# 0022 - Generate Parentheses
# Date: 2024-06-01
# Runtime: 42 ms, Memory: 16.9 MB
# Submission Id: 1274235439


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        ans = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-i-1):
                    ans.append(f"({left}){right}")

        return ans