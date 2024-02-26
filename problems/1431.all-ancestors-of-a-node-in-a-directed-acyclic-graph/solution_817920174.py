# 1431 - All Ancestors of a Node in a Directed Acyclic Graph
# Date: 2022-10-08
# Runtime: 1334 ms, Memory: 30.2 MB
# Submission Id: 817920174


from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # build a graph with reversed edges
        graph = defaultdict(list)
        for p, q in edges:
            graph[q].append(p)
            
        ans = []
        for i in range(n):
            seen = set()
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            ans.append(sorted(seen))
        return ans