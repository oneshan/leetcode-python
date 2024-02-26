# 0046 - Permutations
# Date: 2022-12-06
# Runtime: 68 ms, Memory: 14.1 MB
# Submission Id: 855421878


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        
        def backtracking(start):
            if start == n:
                ans.append(nums[:])
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtracking(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtracking(0)
        return ans