# 0287 - Find the Duplicate Number
# Date: 2023-09-19
# Runtime: 721 ms, Memory: 31 MB
# Submission Id: 1053093467


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def check(target):
            return sum(1 for num in nums if num <= target) > target
        
        left, right = 1, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
