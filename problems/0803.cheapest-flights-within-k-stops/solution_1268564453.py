# 0803 - Cheapest Flights Within K Stops
# Date: 2024-05-26
# Runtime: 91 ms, Memory: 17.9 MB
# Submission Id: 1268564453


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = defaultdict(list)
        for _from , _to, price in flights:
            graph[_from].append((price, _to))

        heap = [(0, 0, src)]  # cost, stops, city
        visited = {}
        while heap:
            cost, stops, city = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops == k + 1:
                continue
            
            if city not in visited or visited[city] > stops:
                visited[city] = stops
                for price, next_city in graph[city]:
                    heapq.heappush(heap, (cost+price, stops+1, next_city))
        
        return -1