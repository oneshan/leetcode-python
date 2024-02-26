# 0605 - Can Place Flowers
# Date: 2023-03-20
# Runtime: 164 ms, Memory: 14.5 MB
# Submission Id: 918579800


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        can_place = 0
        len_bed = len(flowerbed)
        for idx in range(len_bed):
            if flowerbed[idx] == 1:
                continue
            left = (idx == 0) or flowerbed[idx-1] == 0
            right = (idx == len_bed-1) or flowerbed[idx+1] == 0
            if left and right:
                flowerbed[idx] = 1
                can_place += 1
            if can_place == n:
                return True
        return False