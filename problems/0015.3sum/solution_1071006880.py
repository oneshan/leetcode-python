# 0015 - 3Sum
# Date: 2023-10-09
# Runtime: 1304 ms, Memory: 20.6 MB
# Submission Id: 1071006880


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, first_used = set(), set()
            
        n = len(nums)
        for i in range(n):
            if nums[i] in first_used:
                continue
            first_used.add(nums[i])
            seen = set()
            for j in range(i+1, n):
                target = -nums[i]-nums[j]
                if target in seen:
                    ans.add(tuple(sorted((nums[i], nums[j], target))))                    
                seen.add(nums[j])
        return ans