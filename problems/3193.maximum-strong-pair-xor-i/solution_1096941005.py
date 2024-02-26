# 3193 - Maximum Strong Pair XOR I
# Date: 2023-11-12
# Runtime: 203 ms, Memory: 16.2 MB
# Submission Id: 1096941005


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    ans = max(ans, nums[i] ^ nums[j])
        return ans