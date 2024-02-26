# 1039 - Find the Town Judge
# Date: 2024-02-22
# Runtime: 633 ms, Memory: 21.7 MB
# Submission Id: 1182551910


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n+1)
        no_judge = set()
        for a, b in trust:
            no_judge.add(a)
            count[b] += 1
        for i in range(1, n+1):
            if i in no_judge:
                continue
            if count[i] == n-1:
                return i
        return -1