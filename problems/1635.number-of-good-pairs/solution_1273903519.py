# 1635 - Number of Good Pairs
# Date: 2024-06-01
# Runtime: 43 ms, Memory: 16.4 MB
# Submission Id: 1273903519


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter =  Counter()
        ans = 0
        for num in nums:
            ans += counter[num]
            counter[num] += 1
        return ans