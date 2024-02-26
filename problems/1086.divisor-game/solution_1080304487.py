# 1086 - Divisor Game
# Date: 2023-10-21
# Runtime: 33 ms, Memory: 16.1 MB
# Submission Id: 1080304487


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n & 1 == 0