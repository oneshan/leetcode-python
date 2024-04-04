# 0325 - Maximum Size Subarray Sum Equals k
# Date: 2024-03-27
# Runtime: 471 ms, Memory: 60.2 MB
# Submission Id: 1215471850


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        table = {}
        
        curr = ans = 0
        for idx, num in enumerate(nums):
            curr += num
            if curr == k:
                ans = idx + 1
            if curr not in table:
                table[curr] = idx
            if curr - k in table:
                ans = max(ans, idx - table[curr-k])
        return ans