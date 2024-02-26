# 1661 - Minimum Number of Vertices to Reach All Nodes
# Date: 2022-10-06
# Runtime: 1404 ms, Memory: 52.8 MB
# Submission Id: 816563049


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        for p, q in edges:
            ans.discard(q)
        return ans