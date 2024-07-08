# 3431 - Find the Minimum Cost Array Permutation
# Date: 2024-05-12
# Runtime: 2446 ms, Memory: 43.3 MB
# Submission Id: 1255933317


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final_mask = (1 << n) - 1

        @cache
        def recur(mask, prev):
            if mask == final_mask:
                return abs(prev - nums[0]), [prev]
            
            min_score, min_perm = float('inf'), []
            for i in range(1, n):
                if mask & (1 << i) == 0:
                    cost, perm = recur(mask ^ (1 << i), i)
                    cost += abs(prev - nums[i])
                    if cost < min_score:
                        min_score, min_perm = cost, perm
            
            return min_score, [prev] + min_perm
        
        return recur(1, 0)[1]