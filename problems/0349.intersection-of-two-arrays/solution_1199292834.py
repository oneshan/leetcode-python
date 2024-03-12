# 0349 - Intersection of Two Arrays
# Date: 2024-03-10
# Runtime: 40 ms, Memory: 16.8 MB
# Submission Id: 1199292834


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)