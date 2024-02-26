# 0376 - Wiggle Subsequence
# Date: 2022-11-10
# Runtime: 29 ms, Memory: 13.9 MB
# Submission Id: 840745494


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)