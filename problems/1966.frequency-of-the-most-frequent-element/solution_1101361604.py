# 1966 - Frequency of the Most Frequent Element
# Date: 2023-11-18
# Runtime: 1135 ms, Memory: 31.1 MB
# Submission Id: 1101361604


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = ans = curr = 0
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            
            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            
            ans = max(ans, right-left+1)
        return ans