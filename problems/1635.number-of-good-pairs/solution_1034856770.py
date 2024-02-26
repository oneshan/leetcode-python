# 1635 - Number of Good Pairs
# Date: 2023-08-29
# Runtime: 41 ms, Memory: 16.1 MB
# Submission Id: 1034856770


from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        table = defaultdict(int)
        for num in nums:
            ans += table[num]
            table[num] += 1
        return ans