# 2387 - Partition Array Such That Maximum Difference Is K
# Date: 2022-10-10
# Runtime: 2210 ms, Memory: 28.7 MB
# Submission Id: 819180145


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, curr_min = 1, nums[0]
        for num in nums:
            if num > curr_min + k:
                ans += 1
                curr_min = num
        return ans