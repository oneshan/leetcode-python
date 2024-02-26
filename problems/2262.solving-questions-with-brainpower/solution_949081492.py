# 2262 - Solving Questions With Brainpower
# Date: 2023-05-12
# Runtime: 1572 ms, Memory: 62.6 MB
# Submission Id: 949081492


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        
        for i in range(n-2, -1, -1):
            point, skip = questions[i]
            dp[i] = max(
                dp[i+1],  # skip
                point + (dp[i+1+skip] if i+1+skip < n else 0)  # solve
            )
            
        return dp[0]