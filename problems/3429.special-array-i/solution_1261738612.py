# 3429 - Special Array I
# Date: 2024-05-19
# Runtime: 62 ms, Memory: 16.5 MB
# Submission Id: 1261738612


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:        
        n = len(nums)
        for i in range(n-1):
            if (nums[i] & 1) == (nums[i+1] & 1):
                return False
        return True