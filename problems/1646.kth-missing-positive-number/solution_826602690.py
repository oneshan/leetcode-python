# 1646 - Kth Missing Positive Number
# Date: 2022-10-20
# Runtime: 133 ms, Memory: 14 MB
# Submission Id: 826602690


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k