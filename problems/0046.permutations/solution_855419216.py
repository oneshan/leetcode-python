# 0046 - Permutations
# Date: 2022-12-06
# Runtime: 92 ms, Memory: 14.3 MB
# Submission Id: 855419216


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        end_mask = (1 << n) - 1
        ans = []
        
        def backtracking(arr, mask):
            if mask == end_mask:
                ans.append(arr[:])
                return
            for i in range(n):
                bit_mask = 1 << i
                if mask & bit_mask:
                    continue
                arr.append(nums[i])
                backtracking(arr, mask | bit_mask)
                arr.pop()
        
        backtracking([], 0)
        return ans