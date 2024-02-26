# 1813 - Maximum Erasure Value
# Date: 2023-08-30
# Runtime: 1003 ms, Memory: 30 MB
# Submission Id: 1036073767


from collections import defaultdict

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        last_seen = {}
        
        curr = left = ans = 0
        for right, num in enumerate(nums):
            curr += num
            while left <= last_seen.get(num, -1):
                last_seen.pop(nums[left])
                curr -= nums[left]
                left += 1
            last_seen[num] = right
            ans = max(ans, curr)
        return ans