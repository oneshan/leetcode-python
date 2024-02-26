# 0088 - Merge Sorted Array
# Date: 2022-09-15
# Runtime: 74 ms, Memory: 13.8 MB
# Submission Id: 800418675


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        while n > 0:
            if m > 0 and nums1[m-1] >= nums2[n-1]:
                nums1[idx] = nums1[m-1]
                m -= 1
            else:
                nums1[idx] = nums2[n-1]
                n -= 1
            idx -= 1