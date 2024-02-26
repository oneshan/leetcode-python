# 1813 - Maximum Erasure Value
# Date: 2023-08-30
# Runtime: 1064 ms, Memory: 29.6 MB
# Submission Id: 1036070767


from collections import defaultdict

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        curr = left = ans = 0
        for right, num in enumerate(nums):
            curr += num
            count[num] += 1
            while count[num] > 1:
                count[nums[left]] -= 1
                curr -= nums[left]
                left += 1
            ans = max(ans, curr)
        return ans