# 0487 - Max Consecutive Ones II
# Date: 2023-08-13
# Runtime: 336 ms, Memory: 16.6 MB
# Submission Id: 1020317249


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = curr = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > 1:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans