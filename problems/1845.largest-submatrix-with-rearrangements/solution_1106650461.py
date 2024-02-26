# 1845 - Largest Submatrix With Rearrangements
# Date: 2023-11-26
# Runtime: 1133 ms, Memory: 39.6 MB
# Submission Id: 1106650461


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        
        ans = 0
        prev_heights = []
        
        for r in range(len_r):
            heights = []
            seen = set()
            
            for height, c in prev_heights:
                if matrix[r][c] == 1:
                    heights.append((height+1, c))
                seen.add(c)
            
            for c in range(len_c):
                if c not in seen and matrix[r][c] == 1:
                    heights.append((1, c))
                    
            for width, (height, _) in enumerate(heights, 1):
                ans = max(ans, height * width)
                
            prev_heights = heights

        return ans