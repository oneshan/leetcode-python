# 1309 - Sort Items by Groups Respecting Dependencies
# Date: 2023-08-20
# Runtime: 344 ms, Memory: 36.4 MB
# Submission Id: 1026452639


from collections import defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m
        
        for i in range(n):
            for prev in beforeItems[i]:
                item_graph[prev].append(i)
                item_indegree[i] += 1
                
                if group[i] != group[prev]:
                    group_graph[group[prev]].append(group[i])
                    group_indegree[group[i]] += 1
        
        def topo_sort(graph, indegree):
            n = len(graph)
            visited = set()
            result = []
            stack = [i for i in range(n) if indegree[i] == 0]
            while stack:
                curr = stack.pop()
                visited.add(curr)
                result.append(curr)
                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        stack.append(neighbor)
            return result
        
        item_order = topo_sort(item_graph, item_indegree)
        group_order = topo_sort(group_graph, group_indegree)
        
        if len(item_order) != n or len(group_order) != m:
            return []
        
        ordered_groups = defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)
        
        ans = []
        for group_idx in group_order:
            ans += ordered_groups[group_idx]
        return ans