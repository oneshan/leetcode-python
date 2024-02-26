# 1086 - Divisor Game
# Date: 2023-10-21
# Runtime: 69 ms, Memory: 17.6 MB
# Submission Id: 1080304895


class Solution:
    def divisorGame(self, n: int) -> bool:
        
        @cache
        def can_win(num):
            if num <= 1:
                return False
            for i in range(1, (num >> 1) + 1):
                if num % i == 0 and not can_win(num-i):
                    return True
            return False
        
        return can_win(n)