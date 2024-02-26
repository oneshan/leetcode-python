# 0803 - Cheapest Flights Within K Stops
# Date: 2023-09-24
# Runtime: 108 ms, Memory: 17.6 MB
# Submission Id: 1057884316


from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for _from, _to, price in flights:
            graph[_from].append((_to, price))
        
        visited = {}
        heap = [(0, 0, src)]
        while heap:
            cost, stops, city = heapq.heappop(heap)
            if city == dst and stops <= (k+1):
                return cost
            if stops == k+1:
                continue
            if city not in visited or visited[city] > stops:
                visited[city] = stops
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost+price, stops+1, neighbor))
        return -1