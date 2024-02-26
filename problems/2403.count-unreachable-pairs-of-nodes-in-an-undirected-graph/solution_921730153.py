# 2403 - Count Unreachable Pairs of Nodes in an Undirected Graph
# Date: 2023-03-25
# Runtime: 2321 ms, Memory: 75.2 MB
# Submission Id: 921730153


from collections import defaultdict, deque

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:        
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        group = []
        seen = set()
        ans, remains = 0, n
        
        def bfs(node):
            seen.add(i)
            queue = deque([i])
            count = 0
            while queue:
                node = queue.popleft()
                count += 1
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            return count
                        
        for i in range(n):
            if i in seen:
                continue
            count = bfs(i)
            remains -= count
            ans += count * remains
        return ans