# 2026 - Merge Triplets to Form Target Triplet
# Date: 2024-05-25
# Runtime: 1609 ms, Memory: 61 MB
# Submission Id: 1267424589


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        curr = [0, 0, 0]
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            curr[0] = max(curr[0], a)
            curr[1] = max(curr[1], b)
            curr[2] = max(curr[2], c)
        
        return curr == target