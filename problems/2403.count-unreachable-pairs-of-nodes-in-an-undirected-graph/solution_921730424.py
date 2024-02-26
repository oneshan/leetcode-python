# 2403 - Count Unreachable Pairs of Nodes in an Undirected Graph
# Date: 2023-03-25
# Runtime: 2242 ms, Memory: 73.8 MB
# Submission Id: 921730424


from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:        
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        group = []
        seen = set()
        ans, remains = 0, n
        
        def dfs(node):
            seen.add(i)
            stack = deque([i])
            count = 0
            while stack:
                node = stack.pop()
                count += 1
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            return count
                        
        for i in range(n):
            if i in seen:
                continue
            count = dfs(i)
            remains -= count
            ans += count * remains
        return ans