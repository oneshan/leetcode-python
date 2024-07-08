# 0861 - Flipping an Image
# Date: 2024-06-20
# Runtime: 53 ms, Memory: 16.4 MB
# Submission Id: 1294311253


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(image), len(image[0])

        ans = [[0] * len_c for _ in range(len_r)]
        for r in range(len_r):
            for c in range(len_c):
                ans[r][~c] = 1 ^ image[r][c]
        return ans