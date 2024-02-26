# 0733 - Flood Fill
# Date: 2022-11-19
# Runtime: 188 ms, Memory: 14 MB
# Submission Id: 846219576


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        len_r, len_c = len(image), len(image[0])
        origin = image[sr][sc]
        if origin == color:
            return image
        
        stack = [(sr, sc)]
        seen = set([(sr, sc)])
        while stack:
            row, col = stack.pop()
            image[row][col] = color
            for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                new_r, new_c = row+dx, col+dy
                if (0 <= new_r < len_r and 0 <= new_c < len_c
                    and (new_r, new_c) not in seen
                    and image[new_r][new_c] == origin):
                    stack.append((new_r, new_c))
                    seen.add((new_r, new_c))
        return image