# 3227 - Find Missing and Repeated Values
# Date: 2023-12-17
# Runtime: 131 ms, Memory: 16.7 MB
# Submission Id: 1121420706


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        counter = defaultdict(int)
        for i in range(n*n):
            r, c = divmod(i, n)
            counter[grid[r][c]] += 1
        
        a = b = 0
        for i in range(1, n*n+1):
            if counter[i] == 0:
                a = i
            elif counter[i] > 1:
                b = i
        return [b, a]