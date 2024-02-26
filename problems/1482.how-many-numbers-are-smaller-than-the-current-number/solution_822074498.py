# 1482 - How Many Numbers Are Smaller Than the Current Number
# Date: 2022-10-14
# Runtime: 53 ms, Memory: 13.9 MB
# Submission Id: 822074498


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        table = {}        
        for idx, num in enumerate(sorted(nums)):
            if num not in table:
                table[num] = idx
                
        for idx, num in enumerate(nums):
            nums[idx] = table[num]
        return nums