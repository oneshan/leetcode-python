# 0118 - Pascal's Triangle
# Date: 2022-07-13
# Runtime: 66 ms, Memory: 13.9 MB
# Submission Id: 746086057


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = [1 for _ in range(i+1)]
            for j in range(1, i):
                row[j] = ans[-1][j-1] + ans[-1][j]
            ans.append(row)
        return ans