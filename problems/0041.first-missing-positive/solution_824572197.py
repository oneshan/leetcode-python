# 0041 - First Missing Positive
# Date: 2022-10-18
# Runtime: 531 ms, Memory: 28.7 MB
# Submission Id: 824572197


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i