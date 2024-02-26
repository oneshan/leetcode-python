# 1431 - All Ancestors of a Node in a Directed Acyclic Graph
# Date: 2022-10-08
# Runtime: 1990 ms, Memory: 45.9 MB
# Submission Id: 817929981


from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for p, q in edges:
            graph[p].append(q)
            indegree[q] += 1
        
        ans = [set() for _ in range(n)] 
        queue = deque([i for i in range(n) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ans[neighbor].add(node)
                ans[neighbor].update(ans[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [(sorted(list(s))) for s in ans]