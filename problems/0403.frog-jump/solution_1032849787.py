# 0403 - Frog Jump
# Date: 2023-08-27
# Runtime: 105 ms, Memory: 25.5 MB
# Submission Id: 1032849787


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        table = set(stones)
        
        @cache
        def recur(curr_pos, k):
            if curr_pos not in table:
                return False

            if curr_pos == stones[-1]:
                return True
                        
            for next_k in (k-1, k, k+1):
                if next_k > 0 and recur(curr_pos + next_k, next_k):
                    return True
            return False
        
        return recur(0, 0)