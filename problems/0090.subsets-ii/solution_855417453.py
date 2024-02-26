# 0090 - Subsets II
# Date: 2022-12-06
# Runtime: 87 ms, Memory: 14.2 MB
# Submission Id: 855417453


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        
        def backtracking(arr, start):
            ans.append(arr[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                backtracking(arr, i+1)
                arr.pop()
        
        backtracking([], 0)
        return ans