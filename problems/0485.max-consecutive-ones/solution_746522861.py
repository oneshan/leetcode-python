# 0485 - Max Consecutive Ones
# Date: 2022-07-14
# Runtime: 374 ms, Memory: 14.4 MB
# Submission Id: 746522861


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count +=1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)