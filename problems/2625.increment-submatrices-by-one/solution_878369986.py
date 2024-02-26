# 2625 - Increment Submatrices by One
# Date: 2023-01-15
# Runtime: 2943 ms, Memory: 115.6 MB
# Submission Id: 878369986


from collections import defaultdict

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        tmp = [[0 for _ in range(n)] for _ in range(n)]
        add = defaultdict(int)
        minus = defaultdict(int)
        for r1, c1, r2, c2 in queries:
            add[(r1-1, c1-1)] += 1
            add[(r2, c2)] += 1
            minus[(r1-1, c2)] += 1
            minus[(r2, c1-1)] += 1
        
        for r in range(n-1, -1, -1):
            row_add_sum = 0
            row_minus_sum = 0
            for c in range(n-1, -1, -1):
                row_add_sum += add[(r, c)]
                row_minus_sum += minus[(r, c)]
                ans[r][c] = row_add_sum
                tmp[r][c] = row_minus_sum
                if r < n-1:
                    ans[r][c] += ans[r+1][c]
                    tmp[r][c] += tmp[r+1][c]

        for r in range(n):
            for c in range(n):
                ans[r][c] -= tmp[r][c]
        return ans