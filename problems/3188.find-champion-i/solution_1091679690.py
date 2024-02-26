# 3188 - Find Champion I
# Date: 2023-11-05
# Runtime: 474 ms, Memory: 16.9 MB
# Submission Id: 1091679690


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        for i in range(n):
            for j in range(i+1, n):
                if grid[i][j] == 0:
                    break
            else:
                return i