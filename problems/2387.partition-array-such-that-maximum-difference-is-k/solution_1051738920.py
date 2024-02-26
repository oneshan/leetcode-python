# 2387 - Partition Array Such That Maximum Difference Is K
# Date: 2023-09-17
# Runtime: 765 ms, Memory: 31 MB
# Submission Id: 1051738920


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, curr_min = 1, nums[0]
        for num in nums:
            if num - curr_min > k:
                curr_min = num
                ans += 1
        return ans