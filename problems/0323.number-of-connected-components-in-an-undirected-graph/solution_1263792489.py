# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2024-05-21
# Runtime: 83 ms, Memory: 18.3 MB
# Submission Id: 1263792489


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i):
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)

        ans = 0
        seen = set()
        for i in range(n):
            if i in seen:
                continue
            ans += 1
            seen.add(i)
            dfs(i)
        return ans