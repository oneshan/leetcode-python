# 3218 - Find Number of Coins to Place in Tree Nodes
# Date: 2024-05-07
# Runtime: 2789 ms, Memory: 43.2 MB
# Submission Id: 1251764343


from sortedcontainers import SortedList

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        n = len(cost)
        ans = [1] * n

        def dfs(node, parent):
            values = SortedList([cost[node]])
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_values = dfs(neighbor, node)
                for val in child_values:
                    values.add(val)

            while len(values) > 5:
                values.pop(2)

            if len(values) < 3:
                ans[node] = 1
            else:
                ans[node] = max(
                    values[0] * values[1] * values[-1],
                    values[-3] * values[-2] * values[-1],
                    0
                )

            return values

        dfs(0, None)
        return ans