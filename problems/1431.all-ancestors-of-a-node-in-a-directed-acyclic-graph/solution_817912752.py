# 1431 - All Ancestors of a Node in a Directed Acyclic Graph
# Date: 2022-10-08
# Runtime: 1065 ms, Memory: 31.5 MB
# Submission Id: 817912752


from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # build a graph with reversed edges
        graph = defaultdict(list)
        for p, q in edges:
            graph[q].append(p)
        
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        
        ans = []
        for node in range(n):
            seen = set()
            dfs(node)
            seen.discard(node)
            ans.append(sorted(list(seen)))
            
        return ans