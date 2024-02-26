# 1431 - All Ancestors of a Node in a Directed Acyclic Graph
# Date: 2022-10-08
# Runtime: 1957 ms, Memory: 45.8 MB
# Submission Id: 817927897


from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for p, q in edges:
            graph[p].append(q)
            indegree[q] += 1
        
        ans = [set() for _ in range(n)] 
        stack = [i for i in range(n) if indegree[i] == 0]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                ans[neighbor].add(node)
                ans[neighbor].update(ans[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)
        
        return [(sorted(list(s))) for s in ans]