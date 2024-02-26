# 1646 - Kth Missing Positive Number
# Date: 2023-03-06
# Runtime: 47 ms, Memory: 13.9 MB
# Submission Id: 909997171


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= k + mid + 1:
                right = mid - 1
            else:
                left = mid + 1
        return left + k