# 0803 - Cheapest Flights Within K Stops
# Date: 2024-05-26
# Runtime: 98 ms, Memory: 18 MB
# Submission Id: 1268562477


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = defaultdict(list)
        for _from , _to, price in flights:
            graph[_from].append((price, _to))

        heap = [(0, src, 0)]  # cost, city, stops
        visited = {}
        while heap:
            cost, city, stops = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops == k + 1:
                continue
            
            visited[city] = stops
            for next_cost, next_city in graph[city]:
                if next_city not in visited or visited[next_city] > stops:
                    heapq.heappush(heap, (cost + next_cost, next_city, stops + 1))
        
        return -1