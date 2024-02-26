# 1463 - The K Weakest Rows in a Matrix
# Date: 2022-11-03
# Runtime: 288 ms, Memory: 14.3 MB
# Submission Id: 835863686


import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        len_r, len_c = len(mat), len(mat[0])
        
        ans = []
        for c in range(len_c):
            for r in range(len_r):
                if len(ans) == k:
                    return ans
                if mat[r][c] == 0 and (c==0 or mat[r][c-1] == 1):
                    ans.append(r)
        
        
        for r in range(len_r):
            if len(ans) == k:
                break
            if mat[r][-1] == 1:
                ans.append(r)
                
        return ans