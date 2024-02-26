# 2405 - Minimum Number of Keypresses
# Date: 2022-06-22
# Runtime: 117 ms, Memory: 14.8 MB
# Submission Id: 728431963


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        
        mapping = 0
        arr = sorted([(value, key) for key, value in counter.items()], reverse=True)
        
        ans = mul = 0
        for idx, (val, key) in enumerate(arr):
            if idx % 9 == 0:
                mul += 1
            ans += mul * val
        return ans