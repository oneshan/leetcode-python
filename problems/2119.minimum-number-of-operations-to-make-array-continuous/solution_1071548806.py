# 2119 - Minimum Number of Operations to Make Array Continuous
# Date: 2023-10-10
# Runtime: 660 ms, Memory: 35.2 MB
# Submission Id: 1071548806


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = n = len(nums)
        new_nums = sorted(set(nums))
        m = len(new_nums)

        right = 0
        for left in range(m):
            while right < m and new_nums[right] < new_nums[left] + n:
                right += 1
            ans = min(ans, n - (right - left))
        return ans