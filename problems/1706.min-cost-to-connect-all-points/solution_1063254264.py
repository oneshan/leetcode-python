# 1706 - Min Cost to Connect All Points
# Date: 2023-10-01
# Runtime: 800 ms, Memory: 80 MB
# Submission Id: 1063254264


import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        edges = []
        seen = {0}
        for i in range(1, n):
            dist = abs(points[i][0]-points[0][0]) + abs(points[i][1]-points[0][1])
            heapq.heappush(edges, (dist, i))
        
        cost = 0
        while len(seen) < n:
            dist, i = heapq.heappop(edges)
            if i in seen:
                continue
            seen.add(i)
            cost += dist
            for j in range(n):
                if j not in seen:
                    dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                    heapq.heappush(edges, (dist, j))
        
        return cost
        
        