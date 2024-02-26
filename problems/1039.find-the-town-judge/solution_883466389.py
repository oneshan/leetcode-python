# 1039 - Find the Town Judge
# Date: 2023-01-23
# Runtime: 779 ms, Memory: 19.1 MB
# Submission Id: 883466389


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        scores = [0] * (n+1)
        for a, b in trust:
            scores[b] += 1
            scores[a] -= 1
        
        for i in range(1, n+1):
            if scores[i] == n-1:
                return i
        return -1