# 0399 - Evaluate Division
# Date: 2022-12-03
# Runtime: 65 ms, Memory: 14 MB
# Submission Id: 853732969


from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1/value))
        
        def dfs(start, end):
            seen = set([start])
            stack = [(start, 1)]
            while stack:
                node, curr_val = stack.pop()
                if node == end:
                    return curr_val
                for neighbor, val in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, curr_val * val))
            return -1
        
        ans = [-1] * len(queries)
        for idx, (start, end) in enumerate(queries):
            if start not in graph or end not in graph:
                continue
            ans[idx] = dfs(start, end)
        return ans