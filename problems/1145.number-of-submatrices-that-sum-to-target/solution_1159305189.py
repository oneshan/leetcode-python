# 1145 - Number of Submatrices That Sum to Target
# Date: 2024-01-28
# Runtime: 591 ms, Memory: 17.5 MB
# Submission Id: 1159305189


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        
        ps = [[0] * (len_c + 1) for _ in range(len_r + 1)]
        for r in range(1, len_r+1):
            for c in range(1, len_c+1):
                ps[r][c] = ps[r-1][c] + ps[r][c-1] - ps[r-1][c-1] + matrix[r-1][c-1]
        
        ans = 0
        for col1 in range(1, len_c+1):
            for col2 in range(col1, len_c+1):
                hist = defaultdict(int)
                hist[0] = 1
                for row in range(1, len_r+1):
                    curr_sum = ps[row][col2] - ps[row][col1-1]
                    ans += hist[curr_sum - target]
                    hist[curr_sum] += 1
        return ans