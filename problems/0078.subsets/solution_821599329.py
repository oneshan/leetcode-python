# 0078 - Subsets
# Date: 2022-10-13
# Runtime: 69 ms, Memory: 14.1 MB
# Submission Id: 821599329


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        
        def generate(curr, start):
            if start > n:
                return
            ans.append(curr)
            for i in range(start, n):
                generate(curr+[nums[i]], i+1)
        
        generate([], 0)
        return ans