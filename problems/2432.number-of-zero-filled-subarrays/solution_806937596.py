# 2432 - Number of Zero-Filled Subarrays
# Date: 2022-09-24
# Runtime: 1117 ms, Memory: 24.7 MB
# Submission Id: 806937596


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr = ans = 0
        for num in nums:
            if num == 0:
                curr += 1
                ans += curr
            else:
                curr = 0
        return ans