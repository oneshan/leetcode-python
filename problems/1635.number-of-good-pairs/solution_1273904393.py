# 1635 - Number of Good Pairs
# Date: 2024-06-01
# Runtime: 39 ms, Memory: 16.3 MB
# Submission Id: 1273904393


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter =  Counter(nums)
        return sum(freq * (freq-1) // 2 for freq in counter.values() if freq > 1)