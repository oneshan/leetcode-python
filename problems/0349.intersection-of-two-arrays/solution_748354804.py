# 0349 - Intersection of Two Arrays
# Date: 2022-07-16
# Runtime: 79 ms, Memory: 14.2 MB
# Submission Id: 748354804


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))