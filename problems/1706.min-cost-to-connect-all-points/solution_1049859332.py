# 1706 - Min Cost to Connect All Points
# Date: 2023-09-15
# Runtime: 1039 ms, Memory: 79.8 MB
# Submission Id: 1049859332


import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]
        
        def cal_dist(_from, _to):
            return abs(_from[0] - _to[0]) + abs(_from[1] - _to[1])
        
        ans = 0
        visited = set()
        while heap and len(visited) < n:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
                
            visited.add(node)
            ans += weight
            for i in range(n):
                if i not in visited:
                    w = cal_dist(points[node], points[i])
                    heapq.heappush(heap, (w ,i))
        return ans