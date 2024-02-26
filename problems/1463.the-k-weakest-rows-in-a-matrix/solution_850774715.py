# 1463 - The K Weakest Rows in a Matrix
# Date: 2022-11-28
# Runtime: 329 ms, Memory: 14.2 MB
# Submission Id: 850774715


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soliders = [(sum(row), idx) for idx, row in enumerate(mat)]
        return [idx for _, idx in sorted(soliders)[:k]]
            
        