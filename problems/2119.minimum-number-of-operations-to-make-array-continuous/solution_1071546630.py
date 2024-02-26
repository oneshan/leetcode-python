# 2119 - Minimum Number of Operations to Make Array Continuous
# Date: 2023-10-10
# Runtime: 1191 ms, Memory: 35.1 MB
# Submission Id: 1071546630


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = n = len(nums)
        new_nums = sorted(set(nums))
        m = len(new_nums)

        for i in range(m):
            target = new_nums[i] + (n-1)
            left, right = i, m
            while left < right:
                mid = (left + right) // 2
                if new_nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            ans = min(ans, i + (n-left))
        return ans