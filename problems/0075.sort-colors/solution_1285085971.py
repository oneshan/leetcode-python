# 0075 - Sort Colors
# Date: 2024-06-12
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1285085971


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        
        color = 0
        for i in range(len(nums)):
            while counter[color] == 0:
                color += 1
            counter[color] -= 1
            nums[i] = color
                