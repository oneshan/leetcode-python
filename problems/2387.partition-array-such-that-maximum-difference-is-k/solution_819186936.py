# 2387 - Partition Array Such That Maximum Difference Is K
# Date: 2022-10-10
# Runtime: 3368 ms, Memory: 28.5 MB
# Submission Id: 819186936


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx = ans = 0
        while idx < len(nums):
            idx = self.binary_search(nums, nums[idx]+k, idx, len(nums))
            ans += 1
        return ans
    
    def binary_search(self, nums, val, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= val:
                left = mid + 1
            else:
                right = mid
        return left