# 3104 - Happy Students
# Date: 2023-09-17
# Runtime: 508 ms, Memory: 28.7 MB
# Submission Id: 1051424009


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        ans = 0
        for i in range(n-1):
            if nums[i+1] > (i+1) > nums[i]:
                ans += 1
                
        if nums[0] > 0:
            ans += 1
        if nums[-1] < n:
            ans += 1
        return ans