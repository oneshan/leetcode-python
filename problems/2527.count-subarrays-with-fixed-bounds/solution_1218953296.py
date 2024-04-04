# 2527 - Count Subarrays With Fixed Bounds
# Date: 2024-03-31
# Runtime: 763 ms, Memory: 31.2 MB
# Submission Id: 1218953296


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        left = -1
        last_seen = {minK: -1, maxK: -1}
        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                left = idx
            if num in last_seen:
                last_seen[num] = idx
            ans += max(0, min(last_seen.values()) - left)

        return ans