# 3249 - Minimum Number of Operations to Make Array XOR Equal to K
# Date: 2024-04-29
# Runtime: 598 ms, Memory: 31 MB
# Submission Id: 1244515067


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        val = 0
        for num in nums:
            val ^= num
        
        ans = 0
        for i in range(32):
            ans += (val & 1) != (k & 1)
            val >>= 1
            k >>= 1
        return ans