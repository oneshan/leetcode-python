# 2360 - Substring With Largest Variance
# Date: 2023-07-09
# Runtime: 8086 ms, Memory: 16.5 MB
# Submission Id: 989765651


class Solution:
    def largestVariance(self, s: str) -> int:
        counter = [0] * 26
        for ch in s:
            counter[ord(ch)-ord('a')] += 1
        
        ans = 0
        
        for i in range(26):
            if counter[i] == 0:
                continue
            for j in range(26):
                if i == j or counter[j] == 0:
                    continue
                
                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                major_count = minor_count = 0
                
                rest_minor = counter[j]
                for ch in s:
                    if ch == major:
                        major_count += 1
                    if ch == minor:
                        minor_count += 1
                        rest_minor -= 1
                    if minor_count > 0:
                        ans = max(ans, major_count - minor_count)
                    if major_count < minor_count and rest_minor > 0:
                        major_count = minor_count = 0
        return ans