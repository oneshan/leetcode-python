# 1060 - Longest Repeating Substring
# Date: 2023-09-22
# Runtime: 46 ms, Memory: 16.6 MB
# Submission Id: 1056382009


from collections import defaultdict

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        
        def check(max_len):
            seen = set()
            for i in range(n-max_len+1):
                sub_str = s[i:i+max_len]
                if sub_str in seen:
                    return True
                seen.add(sub_str)
            return False
        
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1