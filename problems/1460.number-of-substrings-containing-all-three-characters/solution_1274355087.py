# 1460 - Number of Substrings Containing All Three Characters
# Date: 2024-06-02
# Runtime: 222 ms, Memory: 16.8 MB
# Submission Id: 1274355087


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = count = left = 0
        
        counter = {'a': 0, 'b': 0, 'c': 0}
        for right, ch in enumerate(s):
            counter[ch] += 1
            while min(counter.values()) > 0:
                ans += len(s) - right
                counter[s[left]] -= 1
                left += 1
        return ans