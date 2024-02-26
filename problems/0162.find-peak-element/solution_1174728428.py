# 0162 - Find Peak Element
# Date: 2024-02-14
# Runtime: 44 ms, Memory: 16.8 MB
# Submission Id: 1174728428


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left