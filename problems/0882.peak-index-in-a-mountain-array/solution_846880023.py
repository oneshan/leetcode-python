# 0882 - Peak Index in a Mountain Array
# Date: 2022-11-20
# Runtime: 616 ms, Memory: 27.9 MB
# Submission Id: 846880023


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 1, len(arr)-2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1