# 1730 - Special Array With X Elements Greater Than or Equal X
# Date: 2022-11-25
# Runtime: 40 ms, Memory: 13.9 MB
# Submission Id: 849483123


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left, right = 0, 1000
        while left <= right:
            mid = (left + right) // 2
            total = sum(1 for num in nums if num >= mid)
            if mid == total:
                return mid
            if mid > total:
                right = mid -1
            else:
                left = mid + 1
        return -1