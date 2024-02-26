# 0268 - Missing Number
# Date: 2023-07-26
# Runtime: 149 ms, Memory: 17.8 MB
# Submission Id: 1004446867


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for idx, num in enumerate(nums, 1):
            ans ^= idx ^ num
        return ans