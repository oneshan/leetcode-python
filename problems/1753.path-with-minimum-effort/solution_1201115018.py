# 1753 - Path With Minimum Effort
# Date: 2024-03-12
# Runtime: 903 ms, Memory: 20.1 MB
# Submission Id: 1201115018


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights) #i
        n = len(heights[0]) #j

        def dfs_reach_end(max_effort, seen, i, j):
            if seen[i][j]:
            	return False

            if i == m-1 and j == n-1:
            	return True
                
            seen[i][j] = True
                
            for di, dj in ((0,1),(1,0), (-1,0), (0, -1)):
                if i+di>=m or i+di<0 or j+dj>=n or j+dj<0:
                    continue
                if abs(heights[i+di][j+dj] - heights[i][j])>max_effort:
                    continue
                if dfs_reach_end(max_effort, seen, i+di, j+dj):
                    return True
            return False

        left = 0
        right = 10**6
        res = 10**6
        while left<=right:
            effort_try = left + (right-left) // 2
            seen = [[False]*n for _ in range(m)]
            if dfs_reach_end(effort_try, seen, 0, 0):
                right = effort_try - 1
                res = min(res, effort_try)
            else:
                left = effort_try + 1
        return res