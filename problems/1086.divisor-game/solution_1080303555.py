# 1086 - Divisor Game
# Date: 2023-10-21
# Runtime: 58 ms, Memory: 17.8 MB
# Submission Id: 1080303555


class Solution:
    def divisorGame(self, n: int) -> bool:
        
        @cache
        def recur(num):
            if num <= 1:
                return False
            for i in range(1, (num >> 1) + 1):
                if num % i == 0 and not recur(num-i):
                    return True
            return False
        
        return recur(n)