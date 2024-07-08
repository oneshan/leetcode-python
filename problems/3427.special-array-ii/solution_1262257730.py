# 3427 - Special Array II
# Date: 2024-05-19
# Runtime: 999 ms, Memory: 55.8 MB
# Submission Id: 1262257730


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        locs = [-1]
        for i in range(n-1):
            if nums[i] & 1 == nums[i+1] & 1:
                locs.append(i)

        ans = []
        for _from, _to in queries:
            ans.append(bisect.bisect_left(locs, _from) == bisect.bisect_left(locs, _to))
            
        return ans
                