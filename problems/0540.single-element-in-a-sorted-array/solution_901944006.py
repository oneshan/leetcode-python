# 0540 - Single Element in a Sorted Array
# Date: 2023-02-21
# Runtime: 184 ms, Memory: 23.8 MB
# Submission Id: 901944006


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans