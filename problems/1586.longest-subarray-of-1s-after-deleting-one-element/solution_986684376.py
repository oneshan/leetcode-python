# 1586 - Longest Subarray of 1's After Deleting One Element
# Date: 2023-07-05
# Runtime: 379 ms, Memory: 18.9 MB
# Submission Id: 986684376


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = prev = curr = 0
        for bit in nums:
            if bit:
                curr += 1
                ans = max(ans, prev + curr)
            else:
                prev, curr = curr, 0
        return ans - (ans == len(nums))