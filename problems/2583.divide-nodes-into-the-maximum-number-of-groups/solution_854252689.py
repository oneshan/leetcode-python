# 2583 - Divide Nodes Into the Maximum Number of Groups
# Date: 2022-12-04
# Runtime: 6794 ms, Memory: 18.4 MB
# Submission Id: 854252689


from collections import defaultdict, deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
        def dfs(start):
            stack = [start]
            seen = {start}
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            return seen
        
        def bfs(start):
            queue = deque([start])
            seen = {start}
            seen_level = set()
            
            ans = 0
            while queue:
                ans += 1
                next_level = set()
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor in seen_level:
                            return -1
                        if neighbor in seen:
                            continue
                        seen.add(neighbor)
                        next_level.add(neighbor)
                        queue.append(neighbor)
                seen_level = next_level
            return ans
        
        connected = []
        seen = set()    
        for i in range(1, n+1):
            if i not in seen:
                subgroup = dfs(i)
                seen = seen.union(subgroup)
                connected.append(subgroup)
        
        ans = 0
        for subgroup in connected:
            max_count = -1
            for node in subgroup:
                count = bfs(node)
                max_count = max(max_count, count)
            if max_count == -1:
                return -1
            ans += max_count
        return ans