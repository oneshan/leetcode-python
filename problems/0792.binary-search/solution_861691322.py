# 0792 - Binary Search
# Date: 2022-12-18
# Runtime: 693 ms, Memory: 15.5 MB
# Submission Id: 861691322


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1