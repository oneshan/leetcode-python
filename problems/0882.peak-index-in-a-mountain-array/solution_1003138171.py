# 0882 - Peak Index in a Mountain Array
# Date: 2023-07-25
# Runtime: 581 ms, Memory: 30.3 MB
# Submission Id: 1003138171


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left