# 3249 - Minimum Number of Operations to Make Array XOR Equal to K
# Date: 2024-04-29
# Runtime: 569 ms, Memory: 31 MB
# Submission Id: 1244515279


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        val = 0
        for num in nums:
            val ^= num
        
        return bin(val ^ k).count('1')