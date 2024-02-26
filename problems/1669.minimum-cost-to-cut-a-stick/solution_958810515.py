# 1669 - Minimum Cost to Cut a Stick
# Date: 2023-05-28
# Runtime: 912 ms, Memory: 20.5 MB
# Submission Id: 958810515


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] +  sorted(cuts) + [n]
        
        @cache
        def cost(left, right):
            if right - left == 1:
                return 0
            return min(cost(left, mid) + cost(mid, right) + cuts[right] - cuts[left]
                       for mid in range(left+1, right))
        
        return cost(0, len(cuts)-1)