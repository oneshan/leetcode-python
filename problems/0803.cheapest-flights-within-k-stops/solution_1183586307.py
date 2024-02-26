# 0803 - Cheapest Flights Within K Stops
# Date: 2024-02-23
# Runtime: 97 ms, Memory: 18.2 MB
# Submission Id: 1183586307


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = defaultdict(list)
        for _from, _to, price in flights:
            graph[_from].append((price, _to))

        seen = {}
        heap = [(0, 0, src)]
        while heap:
            cost, stops, city = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops == k+1:
                continue
            if city not in seen or seen[city] > stops:
                seen[city] = stops
                for price, neighbor in graph[city]:
                    heapq.heappush(heap, (cost+price, stops+1, neighbor))

        return -1