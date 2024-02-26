# 0078 - Subsets
# Date: 2022-12-06
# Runtime: 41 ms, Memory: 14.1 MB
# Submission Id: 855416258


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backtracking(arr, start):
            ans.append(arr[:])
            for i in range(start, n):
                arr.append(nums[i])
                backtracking(arr, i+1)
                arr.pop()
                
        backtracking([], 0)
        return ans