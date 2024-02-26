# 1094 - Matrix Cells in Distance Order
# Date: 2023-08-22
# Runtime: 108 ms, Memory: 18.3 MB
# Submission Id: 1028127404


from collections import defaultdict

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        table = defaultdict(list)
        
        for r in range(rows):
            for c in range(cols):
                dist = abs(r-rCenter) + abs(c-cCenter)
                table[dist].append((r, c))
        
        ans = []
        for i in range(rows+cols):
            ans.extend(table[i])
        return ans