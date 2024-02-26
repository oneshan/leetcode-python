# 1060 - Longest Repeating Substring
# Date: 2023-10-27
# Runtime: 50 ms, Memory: 16.2 MB
# Submission Id: 1085451828


from collections import defaultdict

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        nums = [ord(ch) - ord('a') for ch in s]
        n = len(s)
        
        MOD = 1_000_000_007
        
        def check(max_len):
            h = 0
            for i in range(max_len):
                h = (h * 26 + nums[i]) % MOD
                
            seen = {h}
            aL = 26 ** max_len % MOD
            for i in range(n - max_len):
                h = (h * 26 - nums[i] * aL + nums[i+max_len]) % MOD
                if h in seen:
                    return True
                seen.add(h)
            return False
        
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1