# 0088 - Merge Sorted Array
# Date: 2022-05-23
# Runtime: 62 ms, Memory: 13.9 MB
# Submission Id: 705161826


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        while n:
            if m == 0 or nums1[m-1] < nums2[n-1]:
                n -= 1
                nums1[idx] = nums2[n]
            else:
                m -= 1
                nums1[idx] = nums1[m]
            idx -= 1