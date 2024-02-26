# 2625 - Increment Submatrices by One
# Date: 2023-01-15
# Runtime: 2208 ms, Memory: 73.5 MB
# Submission Id: 878373523


from collections import defaultdict

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        table = defaultdict(int)
        for r1, c1, r2, c2 in queries:
            table[(r1-1, c1-1)] += 1
            table[(r2, c2)] += 1
            table[(r1-1, c2)] -= 1
            table[(r2, c1-1)] -= 1
        
        for r in range(n-1, -1, -1):
            row_sum = 0
            for c in range(n-1, -1, -1):
                row_sum += table[(r, c)]
                ans[r][c] = row_sum
                if r < n-1:
                    ans[r][c] += ans[r+1][c]

        return ans