# 1746 - Largest Substring Between Two Equal Characters
# Date: 2023-12-31
# Runtime: 51 ms, Memory: 17.4 MB
# Submission Id: 1132613824


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        table = {}
        ans = -1
        for idx, ch in enumerate(s):
            if ch not in table:
                table[ch] = idx
            else:
                ans = max(ans, idx - table[ch] - 1)
        return ans