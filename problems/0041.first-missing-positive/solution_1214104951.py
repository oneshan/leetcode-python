# 0041 - First Missing Positive
# Date: 2024-03-26
# Runtime: 319 ms, Memory: 30.3 MB
# Submission Id: 1214104951


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        mask = 1 << 32
        for num in nums:
            if num > mask:
                num -= mask
            if 0 <= num-1 < n:
                if nums[num-1] < 0:
                    nums[num-1] = 0
                nums[num-1] |= mask

        for i in range(n):
            if nums[i] < mask:
                return i+1
        return n + 1