# 1003 - Minimum Area Rectangle II
# Date: 2024-05-26
# Runtime: 98 ms, Memory: 17.4 MB
# Submission Id: 1268382280


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        def get_dist(p1, p2):
            return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

        def get_mid(p1, p2):
            return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

        visited = defaultdict(set)
        ans = float('inf')
        n = len(points)

        for i in range(n):
            p1 = tuple(points[i])
            for j in range(i+1, n):
                p2 = tuple(points[j])
                mid = get_mid(p1, p2)
                dist = get_dist(p1, p2)
                for p3, p4 in visited[(mid, dist)]:
                    area = get_dist(p1, p3) * get_dist(p1, p4)
                    ans = min(ans, area)
                visited[(mid, dist)].add((p1, p2))

        return ans if ans != float("inf") else 0