# 0118 - Pascal's Triangle
# Date: 2022-07-13
# Runtime: 59 ms, Memory: 14 MB
# Submission Id: 746083786


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            ans.append([1] + [ans[-1][j-1] + ans[-1][j] for j in range(1, i)] + [1])
        return ans