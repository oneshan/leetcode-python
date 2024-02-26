# 1635 - Number of Good Pairs
# Date: 2023-10-03
# Runtime: 42 ms, Memory: 16.2 MB
# Submission Id: 1065415804


from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        ans = 0
        for num in nums:
            ans += counter[num]
            counter[num] += 1
        return ans