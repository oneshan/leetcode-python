# 1100 - Connecting Cities With Minimum Cost
# Date: 2024-05-26
# Runtime: 498 ms, Memory: 23.8 MB
# Submission Id: 1268531150


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b, cost in connections:
            graph[a].append((cost, b))
            graph[b].append((cost, a))

        heap = [(0, 1)]  # (cost, city)
        visited = set()
        ans = 0
        while heap:
            cost, city = heapq.heappop(heap)
            if city in visited:
                continue
            visited.add(city)
            ans += cost
            for next_cost, next_city in graph[city]:
                if next_city not in visited:
                    heapq.heappush(heap, (next_cost, next_city))

        return ans if len(visited) == n else -1