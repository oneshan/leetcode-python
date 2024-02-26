# 0403 - Frog Jump
# Date: 2023-08-27
# Runtime: 107 ms, Memory: 25.2 MB
# Submission Id: 1032848113


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        table = set(stones)
        
        @cache
        def recur(curr_stone, k):
            if curr_stone == stones[-1]:
                return True
            
            for next_k in (k-1, k, k+1):
                if next_k > 0 and curr_stone + next_k in table and recur(curr_stone + next_k, next_k):
                    return True
            return False
        
        return recur(0, 0)