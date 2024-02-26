# 0163 - Missing Ranges
# Date: 2023-10-10
# Runtime: 37 ms, Memory: 16.4 MB
# Submission Id: 1071553552


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        
        ans = []
        if lower < nums[0]:
            ans.append([lower, nums[0]-1])
        
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            ans.append([nums[i]+1, nums[i+1]-1])
            
        if upper > nums[-1]:
            ans.append([nums[-1]+1, upper])
        return ans