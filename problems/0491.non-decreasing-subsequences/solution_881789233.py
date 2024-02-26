# 0491 - Non-decreasing Subsequences
# Date: 2023-01-20
# Runtime: 238 ms, Memory: 22.7 MB
# Submission Id: 881789233


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        sequence = []
        
        def backtrack(idx):
            if idx == n:
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return
            
            if not sequence or sequence[-1] <= nums[idx]:
                sequence.append(nums[idx])
                backtrack(idx+1)
                sequence.pop()
                
            backtrack(idx+1)
        
        backtrack(0)
        return result