# 1916 - Find Center of Star Graph
# Date: 2024-06-27
# Runtime: 632 ms, Memory: 52.3 MB
# Submission Id: 1301549283


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node1, node2 = edges[0]
        return node1 if node1 in edges[1] else node2