# 0034 - Find First and Last Position of Element in Sorted Array
# Date: 2023-10-09
# Runtime: 92 ms, Memory: 17.6 MB
# Submission Id: 1070704263


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)

        # find leftmost
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        ans[0] = left if 0 <= left < n and nums[left] == target else -1

        # find rightmost
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        left -= 1
        ans[1] = left if 0 <= left < n and nums[left] == target else -1
        
        return ans