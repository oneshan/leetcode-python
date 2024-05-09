# 2036 - Count Pairs in Two Arrays
# Date: 2024-05-08
# Runtime: 743 ms, Memory: 35.1 MB
# Submission Id: 1252664115


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0
        nums = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        nums.sort()

        ans = 0
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] > 0:
                ans += right - left
                right -= 1
            else:
                left += 1
        return ans