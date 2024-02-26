# 1984 - Maximum Distance Between a Pair of Values
# Date: 2022-10-11
# Runtime: 1785 ms, Memory: 32.3 MB
# Submission Id: 820220853


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(start, target):
            left, right = start, len(nums2)-1
            while left < right:
                mid = (left + right + 1) // 2
                if target > nums2[mid]:
                    right = mid - 1
                else:
                    left = mid
            return left
            
        ans = 0
        for i in range(len(nums1)):
            j = binary_search(i, nums1[i])
            if j == len(nums2):
                break
            if nums2[j] >= nums1[i]:
                ans = max(ans, j-i)
        return ans
