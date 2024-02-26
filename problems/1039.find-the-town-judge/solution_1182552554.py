# 1039 - Find the Town Judge
# Date: 2024-02-22
# Runtime: 588 ms, Memory: 21.6 MB
# Submission Id: 1182552554


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        
        count = [0] * (n+1)
        for a, b in trust:
            count[a] -= 1
            count[b] += 1

        for i in range(1, n+1):
            if count[i] == n-1:
                return i
        return -1