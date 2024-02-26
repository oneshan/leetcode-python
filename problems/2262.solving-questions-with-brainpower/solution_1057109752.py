# 2262 - Solving Questions With Brainpower
# Date: 2023-09-23
# Runtime: 1483 ms, Memory: 193.4 MB
# Submission Id: 1057109752


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