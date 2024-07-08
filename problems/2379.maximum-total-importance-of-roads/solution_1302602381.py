# 2379 - Maximum Total Importance of Roads
# Date: 2024-06-28
# Runtime: 1235 ms, Memory: 42.8 MB
# Submission Id: 1302602381


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = defaultdict(int)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        arr = sorted(degree.values(), reverse=True)
        ans = 0
        for cnt in arr:
            ans += n * cnt
            n -= 1
        return ans