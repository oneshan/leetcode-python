# 0118 - Pascal's Triangle
# Date: 2022-10-27
# Runtime: 59 ms, Memory: 14 MB
# Submission Id: 831163859


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows-1)
        last_row = prev[-1]
        
        new_row = [last_row[i]+last_row[i+1] for i in range(len(last_row)-1)]
        new_row = [1] + new_row + [1]
        return prev + [new_row]