# 0803 - Cheapest Flights Within K Stops
# Date: 2023-01-26
# Runtime: 111 ms, Memory: 15.3 MB
# Submission Id: 885625687


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
            if city == dst and stops - 1 <= k:
                return cost
            if city not in visited or visited[city] > stops:
                visited[city] = stops
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost+price, stops+1, neighbor))
        return -1