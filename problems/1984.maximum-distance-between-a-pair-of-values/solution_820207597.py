# 1984 - Maximum Distance Between a Pair of Values
# Date: 2022-10-11
# Runtime: 2087 ms, Memory: 32.5 MB
# Submission Id: 820207597


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        i = ans = 0
        for j in range(len(nums2)):
            while i < len(nums1) and nums1[i] > nums2[j]:
                i += 1
            if i == len(nums1):
                break
            ans = max(ans, j-i)
        return ans