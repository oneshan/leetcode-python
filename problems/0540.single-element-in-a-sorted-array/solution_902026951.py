# 0540 - Single Element in a Sorted Array
# Date: 2023-02-21
# Runtime: 184 ms, Memory: 23.7 MB
# Submission Id: 902026951


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            if mid & 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]