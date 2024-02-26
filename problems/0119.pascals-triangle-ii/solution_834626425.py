# 0119 - Pascal's Triangle II
# Date: 2022-11-01
# Runtime: 60 ms, Memory: 13.8 MB
# Submission Id: 834626425


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j-1]
        return row