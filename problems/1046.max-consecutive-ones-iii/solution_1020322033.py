# 1046 - Max Consecutive Ones III
# Date: 2023-08-13
# Runtime: 501 ms, Memory: 17.1 MB
# Submission Id: 1020322033


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeroes = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans