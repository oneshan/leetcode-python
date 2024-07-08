# 1847 - Largest Subarray Length K
# Date: 2024-06-01
# Runtime: 503 ms, Memory: 28.6 MB
# Submission Id: 1273908726


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        left = curr = 0
        for i in range(1, n-k+1):
            if nums[i] > nums[left+curr]:
                left, curr = i-curr, 0
            elif nums[i] == nums[curr]:
                curr += 1
            if curr == k:
                curr = 0

        return nums[left:left+k]