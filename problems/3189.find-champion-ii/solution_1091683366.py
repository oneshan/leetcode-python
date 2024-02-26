# 3189 - Find Champion II
# Date: 2023-11-05
# Runtime: 835 ms, Memory: 17.5 MB
# Submission Id: 1091683366


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for a, b in edges:
            in_degree[b] += 1
            
        ans = [i for i in range(n) if in_degree[i] == 0]
        return ans[0] if len(ans) == 1 else -1