# 0046 - Permutations
# Date: 2023-08-02
# Runtime: 33 ms, Memory: 16.6 MB
# Submission Id: 1009905804


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        end_mask = (1 << n) - 1
        
        def backtrack(arr, mask):
            if mask == end_mask:
                ans.append(arr[:])
                return

            for i in range(n):
                bit_mask = 1 << i
                if mask & bit_mask:
                    continue
                arr.append(nums[i])
                backtrack(arr, mask | bit_mask)
                arr.pop()
        
        backtrack([], 0)
        return ans