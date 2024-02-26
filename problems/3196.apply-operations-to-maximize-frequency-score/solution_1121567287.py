# 3196 - Apply Operations to Maximize Frequency Score
# Date: 2023-12-17
# Runtime: 799 ms, Memory: 31.3 MB
# Submission Id: 1121567287


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        ans = left = curr = 0
        for right in range(n):
            curr += nums[right] - nums[(left+right)//2]
            while curr > k:
                curr -= nums[(left+right+1)//2] - nums[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans