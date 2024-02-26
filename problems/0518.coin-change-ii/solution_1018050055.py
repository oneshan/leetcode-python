# 0518 - Coin Change II
# Date: 2023-08-11
# Runtime: 497 ms, Memory: 152.3 MB
# Submission Id: 1018050055


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def recur(i, remains):
            if remains == 0:
                return 1
            if i == len(coins):
                return 0
            
            count = recur(i+1, remains)
            if coins[i] <= remains:
                count += recur(i, remains - coins[i])

            return count
        
        return recur(0, amount)