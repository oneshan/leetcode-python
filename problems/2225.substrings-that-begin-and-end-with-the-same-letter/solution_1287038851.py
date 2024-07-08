# 2225 - Substrings That Begin and End With the Same Letter
# Date: 2024-06-13
# Runtime: 122 ms, Memory: 17.2 MB
# Submission Id: 1287038851


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = Counter()
        ans = 0
        for ch in s:
            counter[ch] += 1
            ans += counter[ch]

        return ans