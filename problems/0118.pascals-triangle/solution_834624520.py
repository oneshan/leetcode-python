# 0118 - Pascal's Triangle
# Date: 2022-11-01
# Runtime: 60 ms, Memory: 13.9 MB
# Submission Id: 834624520


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1] + [ans[-1][j-1] + ans[-1][j] for j in range(1, i)] + [1]
            ans.append(row)
        return ans