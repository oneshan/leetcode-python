# 0261 - Graph Valid Tree
# Date: 2024-05-20
# Runtime: 81 ms, Memory: 18.4 MB
# Submission Id: 1262879435


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and not edges:
            return True
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        indegree = [0] * n

        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
            graph[a].append(b)
            graph[b].append(a)

        queue = deque([i for i in range(n) if indegree[i] == 1])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append(neighbor)
        return count == n