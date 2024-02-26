# 1392 - Find the Difference of Two Arrays
# Date: 2023-05-03
# Runtime: 182 ms, Memory: 16.7 MB
# Submission Id: 943628432


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [
            list(nums1 - nums2),
            list(nums2 - nums1),
        ]