# 0001 - Two Sum
# Date: 2022-11-03
# Runtime: 144 ms, Memory: 15.2 MB
# Submission Id: 835903194


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            table[num] = idx
        
        for idx, num in enumerate(nums):
            complement = target - num
            if table.get(complement, idx) != idx:
                return [idx, table[complement]]