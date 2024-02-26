# 1016 - Subarray Sums Divisible by K
# Date: 2023-01-19
# Runtime: 301 ms, Memory: 18.9 MB
# Submission Id: 881216957


from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        table[0] = 1
        
        ans = curr = 0
        for num in nums:
            curr = (curr + num) % k
            ans += table[curr]
            table[curr] += 1
        return ans