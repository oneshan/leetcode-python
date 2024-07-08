# 1730 - Special Array With X Elements Greater Than or Equal X
# Date: 2024-05-27
# Runtime: 40 ms, Memory: 16.3 MB
# Submission Id: 1268957595


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        left, right = 0, len(nums)
        while left <= right:
            mid = (left + right) // 2
            count = sum(num >= mid for num in nums)
            if count == mid:
                return mid
            elif mid > count:
                right = mid - 1
            else:
                left = mid + 1
        return -1

        