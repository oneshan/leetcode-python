# 3218 - Find Number of Coins to Place in Tree Nodes
# Date: 2024-05-07
# Runtime: 2795 ms, Memory: 45.6 MB
# Submission Id: 1251713441


from sortedcontainers import SortedList

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        n = len(cost)
        ans = [1] * n
        values = [SortedList() for _ in range(n)]

        def dfs(node, parent):

            values[node].add(cost[node])
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
                for val in values[neighbor]:
                    values[node].add(val)
            
            while len(values[node]) > 5:
                values[node].pop(2)
            if len(values[node]) >= 3:
                ans[node] = max(
                    0,
                    values[node][0] * values[node][1] * values[node][-1],
                    values[node][-3] * values[node][-2] * values[node][-1],
                )

        dfs(0, None)
        return ans