# 3208 - Count Beautiful Substrings II
# Date: 2023-11-26
# Runtime: 246 ms, Memory: 20.7 MB
# Submission Id: 1106764696


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        
        for i in range(1, k+1):
            if i * i % k == 0:
                length = i * 2
                break
        
        seen = defaultdict(int)
        seen[(length-1, 0)] = 1
        
        ans = diff = 0
        for idx, ch in enumerate(s):
            if ch in {'a', 'e', 'i', 'o', 'u'}:
                diff += 1
            else:
                diff -= 1
            ans += seen[(idx % length, diff)]
            seen[(idx % length, diff)] += 1
        return ans