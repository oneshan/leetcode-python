# 2890 - Count Substrings Without Repeating Character
# Date: 2024-06-22
# Runtime: 284 ms, Memory: 17.5 MB
# Submission Id: 1296513036


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        ans = left = 0

        last_pos = {}
        for right in range(len(s)):
            if last_pos.get(s[right], -1) >= left:
                left = last_pos[s[right]] + 1
            last_pos[s[right]] = right
            ans += right - left + 1
        return ans