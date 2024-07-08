# 1969 - Maximum Number of Accepted Invitations
# Date: 2024-06-01
# Runtime: 767 ms, Memory: 17.6 MB
# Submission Id: 1273875625


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        graph = defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    graph[r].append(c)

        matches = {}

        def dfs(boy):
            for girl in graph[boy]:
                if girl not in seen:
                    seen.add(girl)
                    if girl not in matches or dfs(matches[girl]):
                        matches[girl] = boy
                        return 1
            return 0

        ans = 0
        for boy in graph:
            seen = set()
            ans += dfs(boy)

        return ans