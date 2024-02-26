# 0268 - Missing Number
# Date: 2023-08-22
# Runtime: 124 ms, Memory: 17.7 MB
# Submission Id: 1028355204


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for idx, num in enumerate(nums, 1):
            ans ^= idx ^ num
        return ans