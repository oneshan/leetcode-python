# 0119 - Pascal's Triangle II
# Date: 2022-10-27
# Runtime: 39 ms, Memory: 13.8 MB
# Submission Id: 831396609


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = self.getRow(rowIndex-1)
        row = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            row[i] = prev_row[i-1] + prev_row[i]
        return row