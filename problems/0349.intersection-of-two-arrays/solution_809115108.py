# 0349 - Intersection of Two Arrays
# Date: 2022-09-27
# Runtime: 38 ms, Memory: 14.1 MB
# Submission Id: 809115108


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))