# 1706 - Min Cost to Connect All Points
# Date: 2024-05-26
# Runtime: 611 ms, Memory: 16.9 MB
# Submission Id: 1268525130


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_cost(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        n = len(points)
        ans = 0

        visited = set()
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        while len(visited) < n:
            curr_min = float('inf')
            curr_node = -1
            for i in range(n):
                if i not in visited and curr_min > min_dist[i]:
                    curr_min, curr_node = min_dist[i], i

            ans += curr_min
            visited.add(curr_node)
            for i in range(n):
                cost = get_cost(points[curr_node], points[i])
                if i not in visited and min_dist[i] > cost:
                    min_dist[i] = cost
        
        return ans