# 0268 - Missing Number
# Date: 2022-09-26
# Runtime: 143 ms, Memory: 15.2 MB
# Submission Id: 809109373


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for idx, num in enumerate(nums, 1):
            ans ^= idx ^ num
        return ans