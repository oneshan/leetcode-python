# 1482 - How Many Numbers Are Smaller Than the Current Number
# Date: 2022-10-14
# Runtime: 52 ms, Memory: 13.9 MB
# Submission Id: 822077495


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for num in nums:
            count[num] += 1
        
        for i in range(1, 101):
            count[i] += count[i-1]
        
        for idx, num in enumerate(nums):
            nums[idx] = count[num-1] if num else 0
        return nums