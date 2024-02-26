# 3279 - Alice and Bob Playing Flower Game
# Date: 2024-01-28
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1158786482


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        
        even_x = (n >> 1)
        odd_x = (n >> 1) + (n & 1)
        
        even_y = (m >> 1)
        odd_y = (m >> 1) + (m & 1)
        
        return even_x * odd_y + odd_x * even_y