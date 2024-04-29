# 0863 - Sum of Distances in Tree
# Date: 2024-04-28
# Runtime: 829 ms, Memory: 46.4 MB
# Submission Id: 1243917422


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        count = [1] * n
        ans = [0] * n

        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    dfs2(child, node)
        
        dfs1(0, -1)
        dfs2(0, -1)
        return ans