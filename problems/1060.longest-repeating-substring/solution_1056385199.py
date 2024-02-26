# 1060 - Longest Repeating Substring
# Date: 2023-09-22
# Runtime: 45 ms, Memory: 16.3 MB
# Submission Id: 1056385199


from collections import defaultdict

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        nums = [ord(ch) - ord('a') for ch in s]
        n = len(s)
        
        module = 1 << 25
        
        def check(max_len):
            h = 0
            for i in range(max_len):
                h = (h * 26 + nums[i]) % module
                
            seen = {h}
            aL = 26 ** max_len % module
            for i in range(1, n-max_len+1):
                h = (h * 26 - nums[i-1] * aL + nums[i+max_len-1]) % module
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