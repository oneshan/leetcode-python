# 1969 - Maximum Number of Accepted Invitations
# Date: 2024-06-10
# Runtime: 962 ms, Memory: 18.3 MB
# Submission Id: 1283817886


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        matches = {}

        def dfs(boy):
            for girl in range(len_c):
                if grid[boy][girl] and girl not in seen:
                    seen.add(girl)
                    if girl not in matches or dfs(matches[girl]):
                        matches[girl] = boy
                        return 1
            return 0

        ans = 0
        for boy in range(len_r):
            seen = set()
            ans += dfs(boy)

        return ans