# 0882 - Peak Index in a Mountain Array
# Date: 2022-11-20
# Runtime: 844 ms, Memory: 28 MB
# Submission Id: 846880994


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