# 1925 - Count Nice Pairs in an Array
# Date: 2023-11-21
# Runtime: 667 ms, Memory: 26.7 MB
# Submission Id: 1103208471


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        
        def reverse(num):
            n = 0
            while num:
                num, d = divmod(num, 10)
                n = (n * 10) + d
            return n
        
        ans = 0
        seen = defaultdict(int)
        for num in nums:
            diff = num-reverse(num)
            ans += seen[diff]
            seen[diff] += 1
        return ans % MOD