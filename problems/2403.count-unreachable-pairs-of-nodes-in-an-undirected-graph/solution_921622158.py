# 2403 - Count Unreachable Pairs of Nodes in an Undirected Graph
# Date: 2023-03-25
# Runtime: 2103 ms, Memory: 75.4 MB
# Submission Id: 921622158


from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:        
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
            
        group = []
        seen = set()
        for i in range(n):
            if i in seen:
                continue
            seen.add(i)
            stack = [i]
            count = 0
            while stack:
                node = stack.pop()
                count += 1
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            group.append(count)
            
        ans, remains = 0, n
        for count in group:
            remains -= count
            ans += count * remains
        return ans