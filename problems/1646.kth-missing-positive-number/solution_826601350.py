# 1646 - Kth Missing Positive Number
# Date: 2022-10-20
# Runtime: 100 ms, Memory: 14.1 MB
# Submission Id: 826601350


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k