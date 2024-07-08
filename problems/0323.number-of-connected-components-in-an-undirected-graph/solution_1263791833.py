# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2024-05-21
# Runtime: 90 ms, Memory: 18.6 MB
# Submission Id: 1263791833


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i):
            for j in graph[i]:
                if j not in seen:
                    seen.add(j)
                    dfs(j)

        ans = 0
        seen = set()
        for i in range(n):
            if i in seen:
                continue
            ans += 1
            seen.add(i)
            dfs(i)
        return ans