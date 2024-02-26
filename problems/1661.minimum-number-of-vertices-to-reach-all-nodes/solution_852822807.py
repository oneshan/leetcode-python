# 1661 - Minimum Number of Vertices to Reach All Nodes
# Date: 2022-12-01
# Runtime: 2842 ms, Memory: 52.7 MB
# Submission Id: 852822807


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        for p, q in edges:
            ans.discard(q)
        return ans