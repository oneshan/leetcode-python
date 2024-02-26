# 0491 - Non-decreasing Subsequences
# Date: 2023-01-20
# Runtime: 251 ms, Memory: 22.3 MB
# Submission Id: 881790165


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        
        def backtrack(idx, sequence):
            if idx == n:
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return
            
            if not sequence or sequence[-1] <= nums[idx]:
                backtrack(idx+1, sequence+[nums[idx]])
                
            backtrack(idx+1, sequence)
        
        backtrack(0, [])
        return result