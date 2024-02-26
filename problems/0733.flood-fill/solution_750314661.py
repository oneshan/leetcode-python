# 0733 - Flood Fill
# Date: 2022-07-18
# Runtime: 130 ms, Memory: 14.2 MB
# Submission Id: 750314661


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        if image[sr][sc] == color:
            return image
        
        len_r, len_c = len(image), len(image[0])
        old_color = image[sr][sc]
        
        def dfs(r, c):
            if image[r][c] != old_color: return
            image[r][c] = color
            if r > 0: dfs(r-1, c)
            if c > 0: dfs(r, c-1)
            if r < len_r -1: dfs(r+1, c)
            if c < len_c -1: dfs(r, c+1)
        
        dfs(sr, sc)
        return image