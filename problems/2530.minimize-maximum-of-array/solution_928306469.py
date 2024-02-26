# 2530 - Minimize Maximum of Array
# Date: 2023-04-05
# Runtime: 817 ms, Memory: 26.2 MB
# Submission Id: 928306469


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = curr_sum = 0
        for idx, num in enumerate(nums):
            curr_sum += num
            ans = max(ans, math.ceil(curr_sum / (idx+1)))
        return ans