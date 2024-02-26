# 0275 - H-Index II
# Date: 2023-10-29
# Runtime: 140 ms, Memory: 23.1 MB
# Submission Id: 1086638878


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid + 1
        return n - left