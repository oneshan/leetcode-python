# 1646 - Kth Missing Positive Number
# Date: 2022-11-24
# Runtime: 50 ms, Memory: 14.1 MB
# Submission Id: 849082606


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