# 0733 - Flood Fill
# Date: 2022-07-18
# Runtime: 124 ms, Memory: 14.1 MB
# Submission Id: 750311285


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        if image[sr][sc] == color:
            return image
        
        seen = set()
        stack = [(sr, sc)]
        o_color = image[sr][sc]
        len_r, len_c = len(image), len(image[0])
        
        while stack:
            r, c = stack.pop()
            if (r,c) in seen:
                continue
            seen.add((r, c))
            image[r][c] = color

            if r > 0 and image[r-1][c] == o_color:
                stack.append((r-1, c))
            if c > 0 and image[r][c-1] == o_color:
                stack.append((r, c-1))
            if r < len_r-1 and image[r+1][c] == o_color:
                stack.append((r+1, c))
            if c < len_c-1 and image[r][c+1] == o_color:
                stack.append((r, c+1))
        return image