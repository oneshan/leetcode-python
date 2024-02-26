# 0118 - Pascal's Triangle
# Date: 2023-09-08
# Runtime: 46 ms, Memory: 16.3 MB
# Submission Id: 1043486882


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1] + [ans[-1][j-1] + ans[-1][j] for j in range(1, i)] + [1]
            ans.append(row)
        return ans