# 0792 - Binary Search
# Date: 2022-07-16
# Runtime: 439 ms, Memory: 15.5 MB
# Submission Id: 748348292


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1