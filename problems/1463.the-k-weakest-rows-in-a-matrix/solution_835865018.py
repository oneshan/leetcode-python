# 1463 - The K Weakest Rows in a Matrix
# Date: 2022-11-03
# Runtime: 294 ms, Memory: 14.3 MB
# Submission Id: 835865018


import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        for idx, row in enumerate(mat):
            soldiers.append((sum(row), idx))   
        soldiers.sort()
        
        return [soldiers[i][1] for i in range(k)]