# 2121 - Find if Path Exists in Graph
# Date: 2022-12-19
# Runtime: 4744 ms, Memory: 116.3 MB
# Submission Id: 861891546


from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        queue = deque([source])
        seen = {source}
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False