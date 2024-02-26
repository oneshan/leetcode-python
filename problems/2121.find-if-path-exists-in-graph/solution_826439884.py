# 2121 - Find if Path Exists in Graph
# Date: 2022-10-20
# Runtime: 4008 ms, Memory: 106.3 MB
# Submission Id: 826439884


from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            
        queue = deque([source])
        seen = set([source])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True
                if neighbor in seen:
                    continue
                queue.append(neighbor)
                seen.add(neighbor)
        return False