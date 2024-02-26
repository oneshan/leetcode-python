# 2557 - Number of Subarrays With LCM Equal to K
# Date: 2022-11-13
# Runtime: 3437 ms, Memory: 14.1 MB
# Submission Id: 842397160


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def compute_gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        ans = 0
        n = len(nums)
        for i in range(n):
            lcm = nums[i]
            for j in range(i, n):
                gcd = compute_gcd(lcm, nums[j])
                product = lcm * nums[j]
                lcm = product // gcd
                if lcm == k:
                    ans += 1
        return ans