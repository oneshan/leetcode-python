# 1661 - Minimum Number of Vertices to Reach All Nodes
# Date: 2023-05-18
# Runtime: 1219 ms, Memory: 55.2 MB
# Submission Id: 952526818


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        for p, q in edges:
            ans.discard(q)
        return ans