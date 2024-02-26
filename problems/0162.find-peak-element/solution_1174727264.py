# 0162 - Find Peak Element
# Date: 2024-02-14
# Runtime: 53 ms, Memory: 16.7 MB
# Submission Id: 1174727264


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i
        return n-1