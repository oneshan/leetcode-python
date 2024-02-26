# 0004 - Median of Two Sorted Arrays
# Date: 2023-09-21
# Runtime: 99 ms, Memory: 17.7 MB
# Submission Id: 1055511313


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        
        def find_k(idx1, idx2, k):
            if idx1 >= len1:
                return nums2[idx2 + k - 1]
            if idx2 >= len2:
                return nums1[idx1 + k - 1]

            if k == 1:
                return min(nums1[idx1], nums2[idx2])

            next_idx1 = idx1 + (k // 2) - 1
            next_idx2 = idx2 + (k // 2) - 1
            v1 = nums1[next_idx1] if next_idx1 < len1 else float('inf')
            v2 = nums2[next_idx2] if next_idx2 < len2 else float('inf')
            if v1 > v2:
                return find_k(idx1, next_idx2+1, k - (k // 2))
            return find_k(next_idx1+1, idx2, k - (k // 2))
        
        median = find_k(0, 0, (len1 + len2) // 2 + 1)
        if (len1 + len2) & 1:
            return median
        
        median += find_k(0, 0, (len1 + len2) // 2)
        return median / 2