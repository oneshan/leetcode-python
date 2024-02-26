# 0803 - Cheapest Flights Within K Stops
# Date: 2023-01-26
# Runtime: 106 ms, Memory: 15.4 MB
# Submission Id: 885620380


from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for _from, _to, price in flights:
            graph[_from].append((_to, price))
        
        queue = deque([(src, 0, k)])
        prices = [float('inf')] * n
        
        while queue:
            city, cost, stops = queue.popleft()
            for neighbor, price in graph[city]:
                if cost + price < prices[neighbor]:
                    prices[neighbor] = cost + price
                    if stops > 0:
                        queue.append((neighbor, cost+price, stops-1))
        return -1 if prices[dst] == float('inf') else prices[dst]