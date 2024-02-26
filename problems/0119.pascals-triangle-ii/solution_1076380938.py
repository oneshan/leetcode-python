# 0119 - Pascal's Triangle II
# Date: 2023-10-16
# Runtime: 41 ms, Memory: 16.3 MB
# Submission Id: 1076380938


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        row = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j-1]
        return row