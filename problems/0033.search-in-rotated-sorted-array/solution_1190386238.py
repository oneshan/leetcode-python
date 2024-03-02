# 0033 - Search in Rotated Sorted Array
# Date: 2024-03-01
# Runtime: 46 ms, Memory: 16.9 MB
# Submission Id: 1190386238


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:  # [left...mid] sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # [mid+1...right] sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1