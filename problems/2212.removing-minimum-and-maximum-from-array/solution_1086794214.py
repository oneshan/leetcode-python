# 2212 - Removing Minimum and Maximum From Array
# Date: 2023-10-29
# Runtime: 772 ms, Memory: 31.3 MB
# Submission Id: 1086794214


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        min_idx = max_idx = 0
        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
                
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        return min(
            right + 1,
            n - left,
            (left + 1) + (n - right)
        )