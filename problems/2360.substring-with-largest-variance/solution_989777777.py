# 2360 - Substring With Largest Variance
# Date: 2023-07-09
# Runtime: 7183 ms, Memory: 16.5 MB
# Submission Id: 989777777


from collections import Counter

class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        
        ans = 0
        for major in counter.keys():
            for minor in counter.keys():
                if major == minor:
                    continue
                    
                diff, has_minor = 0, False
                rest_minor = counter[minor]
                
                for ch in s:
                    if ch == major:
                        diff += 1
                    if ch == minor:
                        diff -= 1
                        rest_minor -= 1
                        has_minor = True
                    
                    if has_minor:
                        ans = max(ans, diff)
                        
                    if diff < 0 and rest_minor > 0:
                        diff, has_minor = 0, False
        return ans