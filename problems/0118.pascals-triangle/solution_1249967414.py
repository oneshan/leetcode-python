# 0118 - Pascal's Triangle
# Date: 2024-05-05
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1249967414


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(ans[-1][j-1] + ans[-1][j])
            row.append(1)
            ans.append(row)
        return ans