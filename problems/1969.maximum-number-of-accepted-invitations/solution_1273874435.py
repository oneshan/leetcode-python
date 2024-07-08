# 1969 - Maximum Number of Accepted Invitations
# Date: 2024-06-01
# Runtime: 954 ms, Memory: 18.3 MB
# Submission Id: 1273874435


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        len_b, len_g = len(grid), len(grid[0])
        matches = {}

        def dfs(boy):
            for girl in range(len_g):
                if grid[boy][girl] and girl not in seen:
                    seen.add(girl)
                    if girl not in matches or dfs(matches[girl]):
                        matches[girl] = boy
                        return 1
            return 0

        ans = 0
        for boy in range(len_b):
            seen = set()
            ans += dfs(boy)

        return ans