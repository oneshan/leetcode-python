# 1730 - Special Array With X Elements Greater Than or Equal X
# Date: 2022-11-25
# Runtime: 104 ms, Memory: 13.8 MB
# Submission Id: 849484229


from collections import Counter

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count, nums = 0, Counter(nums)
        for i in range(1001, -1, -1):
            count += nums[i]
            if count == i: 
                return count
        return -1