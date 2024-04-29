# 3397 - Find the Integer Added to Array I
# Date: 2024-04-28
# Runtime: 52 ms, Memory: 16.5 MB
# Submission Id: 1243722011


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return (sum(nums2) - sum(nums1)) // len(nums1)