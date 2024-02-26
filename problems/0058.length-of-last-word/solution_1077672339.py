# 0058 - Length of Last Word
# Date: 2023-10-18
# Runtime: 44 ms, Memory: 16.3 MB
# Submission Id: 1077672339


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans, idx = 0, len(s)-1
        while idx >= 0:
            if s[idx] != ' ':
                ans += 1
            elif ans > 0:
                return ans
            idx -= 1
        return ans