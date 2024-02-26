# 1019 - Squares of a Sorted Array
# Date: 2022-09-15
# Runtime: 431 ms, Memory: 16.3 MB
# Submission Id: 800404536


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num * num for num in nums)