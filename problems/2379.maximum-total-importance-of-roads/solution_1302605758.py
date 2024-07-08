# 2379 - Maximum Total Importance of Roads
# Date: 2024-06-28
# Runtime: 1226 ms, Memory: 41.7 MB
# Submission Id: 1302605758


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        buckets = [0] * (n+1)
        for cnt in degree:
            buckets[cnt] += 1
        
        ans = 0
        for i in range(n, 0, -1):
            while buckets[i]:
                ans += n * i
                n -= 1
                buckets[i] -= 1
        return ans