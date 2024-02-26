# 1925 - Count Nice Pairs in an Array
# Date: 2023-11-21
# Runtime: 679 ms, Memory: 29.9 MB
# Submission Id: 1103206880


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        
        @cache        
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