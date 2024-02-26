# 0661 - Image Smoother
# Date: 2023-12-19
# Runtime: 496 ms, Memory: 17.1 MB
# Submission Id: 1123063430


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(img), len(img[0])
        
        ans = [[0] * len_c for _ in range(len_r)]
        for r in range(len_r):
            for c in range(len_c):
                _sum = _count = 0
                for tr in (r-1, r, r+1):
                    for tc in (c-1, c, c+1):
                        if 0 <= tr < len_r and 0 <= tc < len_c:
                            _sum += img[tr][tc]
                            _count += 1
                ans[r][c] = _sum // _count
        return ans