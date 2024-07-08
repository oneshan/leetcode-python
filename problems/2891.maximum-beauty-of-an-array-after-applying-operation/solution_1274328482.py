# 2891 - Maximum Beauty of an Array After Applying Operation
# Date: 2024-06-01
# Runtime: 891 ms, Memory: 30.5 MB
# Submission Id: 1274328482


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = left = 0
        
        for right, num in enumerate(nums):
            while num > nums[left] + 2 * k:
                left += 1
            ans = max(ans, right-left+1)
        return ans