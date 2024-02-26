# 2405 - Minimum Number of Keypresses
# Date: 2022-06-22
# Runtime: 175 ms, Memory: 14.6 MB
# Submission Id: 728431131


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        
        mapping = 0
        arr = sorted([(value, key) for key, value in counter.items()], reverse=True)
        
        ans = len(s)
        for idx, (val, key) in enumerate(arr):
            ans += (idx // 9) * val
        return ans