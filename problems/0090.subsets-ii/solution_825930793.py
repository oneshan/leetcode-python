# 0090 - Subsets II
# Date: 2022-10-19
# Runtime: 45 ms, Memory: 14.2 MB
# Submission Id: 825930793


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        
        def recur(curr, start):
            ans.append(curr)
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                recur(curr+[nums[i]], i + 1)
        
        recur([], 0)
        return ans