# 0403 - Frog Jump
# Date: 2023-08-27
# Runtime: 270 ms, Memory: 35.8 MB
# Submission Id: 1032846043


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        
        target = stones[-1]
        table = set(stones)
        
        @cache
        def recur(curr_stone, k):
            if curr_stone == target:
                return True
            can_do = False
            for diff in (k-1, k, k+1):
                if diff > 0 and curr_stone + diff in table:
                    can_do |= recur(curr_stone + diff, diff)
            return can_do
        
        return recur(0, 0)