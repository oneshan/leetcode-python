# 0078 - Subsets
# Date: 2022-10-13
# Runtime: 54 ms, Memory: 14 MB
# Submission Id: 821602100


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [curr + [num] for curr in ans]
        
        return ans