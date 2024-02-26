# 1984 - Maximum Distance Between a Pair of Values
# Date: 2022-11-29
# Runtime: 4468 ms, Memory: 32.4 MB
# Submission Id: 851792628


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        len_1, len_2 = len(nums1), len(nums2)
        
        def binary_search(i, target):
            left, right = i, len_2 - 1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] < target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        
        ans = 0
        for i in range(len_1):
            j = binary_search(i, nums1[i])
            ans = max(ans, j-i)
        return ans