# 0047 - Permutations II
# Date: 2022-12-06
# Runtime: 156 ms, Memory: 14.4 MB
# Submission Id: 855423398


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def backtracking(start):
            if start == n:
                ans.append(nums[:])
                return
            
            seen = set()
            for i in range(start, n):
                if nums[i] in seen:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                backtracking(start+1)
                nums[start], nums[i] = nums[i], nums[start]
                seen.add(nums[i])
            
            
        backtracking(0)
        return ans