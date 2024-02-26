# 0803 - Cheapest Flights Within K Stops
# Date: 2023-10-02
# Runtime: 265 ms, Memory: 17.5 MB
# Submission Id: 1065060004


from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        
        for i in range(k+1):
            temp = dist[:]
            for _from, _to, cost in flights:
                if dist[_from] != float('inf'):
                    temp[_to] = min(temp[_to], dist[_from] + cost)
            dist = temp
            
        return dist[dst] if dist[dst] != float('inf') else -1