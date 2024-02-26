# 2443 - Check if There is a Valid Partition For The Array
# Date: 2023-08-13
# Runtime: 834 ms, Memory: 111.1 MB
# Submission Id: 1019718941


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def recur(i):
            if i == -1:
                return True
            
            ans = False
            if i > 0 and nums[i] == nums[i-1]:
                ans |= recur(i-2)
            if i > 1 and nums[i] == nums[i-1] == nums[i-2]:
                ans |= recur(i-3)
            if i > 1 and nums[i] == nums[i-1] + 1 == nums[i-2] + 2:
                ans |= recur(i-3)
            return ans
        
        return recur(n-1)