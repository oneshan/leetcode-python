# 3190 - Minimum Operations to Maximize Last Elements in Arrays
# Date: 2023-11-12
# Runtime: 149 ms, Memory: 16.5 MB
# Submission Id: 1096982964


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        max_last = max(nums1[-1], nums2[-1])
        min_last = min(nums1[-1], nums2[-1])
        both_small = swap = no_swap = 0
        for i in range(n-1):
            if nums1[i] > max_last or nums2[i] > max_last:
                return -1
            if nums1[i] > min_last and nums2[i] > min_last:
                return -1
            if nums1[i] <= min_last and nums2[i] <= min_last:
                both_small += 1
            elif nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
                no_swap += 1
            else:
                swap += 1

        return min(
            swap,
            no_swap + 1
        )