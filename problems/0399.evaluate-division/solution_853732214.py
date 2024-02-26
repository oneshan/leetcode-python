# 0399 - Evaluate Division
# Date: 2022-12-03
# Runtime: 28 ms, Memory: 13.9 MB
# Submission Id: 853732214


from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1/value))
        
        ans = [-1] * len(queries)
        for idx, (start, end) in enumerate(queries):
            if start not in graph or end not in graph:
                continue
            seen = set([start])
            stack = [(start, 1)]
            while stack:
                node, curr_val = stack.pop()
                if node == end:
                    ans[idx] = curr_val
                    break
                for neighbor, val in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, curr_val * val))
        return ans