# 0004 - Median of Two Sorted Arrays
# Date: 2024-06-12
# Runtime: 85 ms, Memory: 16.8 MB
# Submission Id: 1285645655


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        middle = (len1 + len2 + 1) // 2
        left, right = 0, len(nums1)
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = middle - mid1

            left1 = nums1[mid1-1] if mid1 >= 1 else float('-inf')
            left2 = nums2[mid2-1] if mid2 >= 1 else float('-inf')
            right1 = nums1[mid1] if mid1 < len1 else float('inf')
            right2 = nums2[mid2] if mid2 < len2 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (len1 + len2) & 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            
            if left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1