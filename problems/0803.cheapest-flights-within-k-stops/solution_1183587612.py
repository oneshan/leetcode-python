# 0803 - Cheapest Flights Within K Stops
# Date: 2024-02-23
# Runtime: 163 ms, Memory: 17.6 MB
# Submission Id: 1183587612


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        
        dist = [float('inf')] * n
        dist[src] = 0
        for _ in range(k+1):
            temp = dist[:]
            for _from, _to, price in flights:
                temp[_to] = min(temp[_to], dist[_from] + price)
            dist = temp

        return dist[dst] if dist[dst] != float('inf') else -1