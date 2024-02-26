# 2596 - Add Edges to Make Degrees of All Nodes Even
# Date: 2022-12-18
# Runtime: 4476 ms, Memory: 55.9 MB
# Submission Id: 861632298


from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        odd_nodes = {node for node in graph if len(graph[node]) & 1}
        odd_count = len(odd_nodes)
        
        if odd_count == 0:
            return True
        
        if odd_count == 2:
            a, b = odd_nodes
            for k in graph:
                if k not in graph[a] and k not in graph[b]:
                    return True 
        elif odd_count == 4:
            a, b, c, d = odd_nodes
            if ((a not in graph[b] and c not in graph[d])
                or (a not in graph[c] and b not in graph[d])
                or (a not in graph[d] and b not in graph[c])):
                return True    
        return False
