# 1003 - Minimum Area Rectangle II
# Date: 2024-05-26
# Runtime: 90 ms, Memory: 17.3 MB
# Submission Id: 1268372009


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        def get_dist(p1, p2):
            return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

        def get_mid(p1, p2):
            return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

        table = defaultdict(set)
        n = len(points)
        for i in range(n):
            p1 = tuple(points[i])
            for j in range(i+1, n):
                p2 = tuple(points[j])
                dist = get_dist(p1, p2)
                mid = get_mid(p1, p2)
                table[(dist, mid)].add((p1, p2))

        ans = float('inf')
        for sub_points in table.values():
            if len(sub_points) == 1:
                continue
            for p1, p2 in sub_points:
                for p3, p4 in sub_points:
                    if (p1, p2) == (p3, p4):
                        continue
                    
                    side1 = get_dist(p1, p3)
                    side2 = get_dist(p1, p4)
                    ans = min(ans, side1 * side2)

        return ans if ans != float('inf') else 0