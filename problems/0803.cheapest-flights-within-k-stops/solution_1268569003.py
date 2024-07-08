# 0803 - Cheapest Flights Within K Stops
# Date: 2024-05-26
# Runtime: 225 ms, Memory: 17.6 MB
# Submission Id: 1268569003


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k+1):
            next_cost = cost[:]
            for _from, _to, price in flights:
                if cost[_from] != float('inf'):
                    next_cost[_to] = min(next_cost[_to], cost[_from] + price)
            cost = next_cost

        return cost[dst] if cost[dst] != float('inf') else -1