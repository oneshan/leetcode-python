# 1431 - All Ancestors of a Node in a Directed Acyclic Graph
# Date: 2024-06-29
# Runtime: 451 ms, Memory: 47.9 MB
# Submission Id: 1303507065


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        indegree = [0] * n
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            indegree[end] += 1
        
        ans = defaultdict(set)
        queue = deque([i for i in range(n) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ans[neighbor].add(node)
                ans[neighbor].update(ans[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return [sorted(ans[i]) for i in range(n)]