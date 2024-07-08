# 1460 - Number of Substrings Containing All Three Characters
# Date: 2024-06-02
# Runtime: 216 ms, Memory: 17 MB
# Submission Id: 1274356840


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = count = left = 0
        
        counter = {'a': 0, 'b': 0, 'c': 0}
        for right, ch in enumerate(s):
            counter[ch] += 1
            while min(counter.values()) > 0:
                counter[s[left]] -= 1
                left += 1
            ans += left
        return ans