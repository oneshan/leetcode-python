# 0034 - Find First and Last Position of Element in Sorted Array
# Date: 2024-03-06
# Runtime: 86 ms, Memory: 17.8 MB
# Submission Id: 1195355935


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums:
            return ans

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        ans[0] = left if nums[left] == target else -1


        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        ans[1] = left if nums[left] == target else -1

        return ans