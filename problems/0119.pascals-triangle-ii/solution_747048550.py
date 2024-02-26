# 0119 - Pascal's Triangle II
# Date: 2022-07-14
# Runtime: 51 ms, Memory: 13.8 MB
# Submission Id: 747048550


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            ans[1:i] = [ans[j - 1] + ans[j] for j in range(1, i)]
        return ans