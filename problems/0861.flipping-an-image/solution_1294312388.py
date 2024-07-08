# 0861 - Flipping an Image
# Date: 2024-06-20
# Runtime: 51 ms, Memory: 16.4 MB
# Submission Id: 1294312388


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(image), len(image[0])

        for r in range(len_r):
            for c in range((len_c+1)>>1):
                image[r][~c], image[r][c] = image[r][c] ^ 1, image[r][~c] ^ 1
        return image