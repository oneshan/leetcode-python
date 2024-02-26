# 2262 - Solving Questions With Brainpower
# Date: 2023-05-12
# Runtime: 1780 ms, Memory: 193.2 MB
# Submission Id: 949075424


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            point, skip = questions[i]
            return max(dp(i+1), point + dp(i+1+skip))
        
        return dp(0)