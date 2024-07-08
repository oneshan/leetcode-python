# 1916 - Find Center of Star Graph
# Date: 2024-06-27
# Runtime: 686 ms, Memory: 52.2 MB
# Submission Id: 1301551242


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
        
        for node, count in degree.items():
            if count == len(edges):
                return node
        return -1