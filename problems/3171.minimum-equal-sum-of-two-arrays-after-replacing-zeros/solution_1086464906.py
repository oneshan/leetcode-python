# 3171 - Minimum Equal Sum of Two Arrays After Replacing Zeros
# Date: 2023-10-29
# Runtime: 967 ms, Memory: 36.3 MB
# Submission Id: 1086464906


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        def get_sum_and_zeros(nums):
            total = zero = 0
            for num in nums:
                total += num
                zero += 1 if num == 0 else 0
            return total, zero
        
        s1, z1 = get_sum_and_zeros(nums1)
        s2, z2 = get_sum_and_zeros(nums2)
        s1 += z1
        s2 += z2
        if s1 > s2 and z2 == 0:
            return -1
        if s2 > s1 and z1 == 0:
            return -1
        return max(s1, s2)