# 0268 - Missing Number
# Date: 2024-02-20
# Runtime: 116 ms, Memory: 17.8 MB
# Submission Id: 1180509412


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for idx, num in enumerate(nums, 1):
            ans ^= idx ^ num
        return ans