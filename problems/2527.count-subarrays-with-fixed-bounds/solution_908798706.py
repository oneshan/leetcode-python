# 2527 - Count Subarrays With Fixed Bounds
# Date: 2023-03-04
# Runtime: 876 ms, Memory: 28.6 MB
# Submission Id: 908798706


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_pos = max_pos = left = -1
        
        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                left = idx
            if num == minK:
                min_pos = idx
            if num == maxK:
                max_pos = idx
            ans += max(0, min(min_pos, max_pos) - left)
        
        return ans