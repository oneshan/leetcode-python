# 2432 - Number of Zero-Filled Subarrays
# Date: 2023-03-21
# Runtime: 1071 ms, Memory: 24.5 MB
# Submission Id: 919137207


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = zeroes = 0
        for num in nums:
            if num:
                zeroes = 0
            else:
                zeroes += 1
                ans += zeroes
        return ans