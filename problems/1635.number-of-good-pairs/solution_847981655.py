# 1635 - Number of Good Pairs
# Date: 2022-11-22
# Runtime: 43 ms, Memory: 13.8 MB
# Submission Id: 847981655


from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table = defaultdict(int)
        ans = 0
        for num in nums:
            ans += table[num]
            table[num] += 1
        return ans