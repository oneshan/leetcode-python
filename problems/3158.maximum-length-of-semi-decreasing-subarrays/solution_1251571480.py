# 3158 - Maximum Length of Semi-Decreasing Subarrays
# Date: 2024-05-07
# Runtime: 699 ms, Memory: 37.8 MB
# Submission Id: 1251571480


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        arr = [(num, idx) for idx, num in enumerate(nums)]
        arr.sort(reverse=True)

        ans = 0
        curr_min = 100001
        for _, idx in arr:
            ans = max(ans, idx - curr_min + 1)
            curr_min = min(idx, curr_min)
            
        return ans