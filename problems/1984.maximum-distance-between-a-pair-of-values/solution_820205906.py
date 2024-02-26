# 1984 - Maximum Distance Between a Pair of Values
# Date: 2022-10-11
# Runtime: 2675 ms, Memory: 30.5 MB
# Submission Id: 820205906


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        i = ans = 0
        for j in range(len(nums2)):
            while i <= j and i < len(nums1) and nums1[i] > nums2[j]:
                i += 1
            if i == len(nums1):
                break
            if i <= j:
                ans = max(ans, j-i)
        return ans