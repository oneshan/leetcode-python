# 0424 - Longest Repeating Character Replacement
# Date: 2022-07-24
# Runtime: 166 ms, Memory: 13.9 MB
# Submission Id: 755480037


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {}
        left = ans = 0
        for right in range(len(s)):
            table[s[right]] = table.get(s[right], 0) + 1
            curr_len = right - left + 1
            if curr_len - max(table.values()) <= k:
                ans = max(ans, curr_len)
            else:  # slide the window
                table[s[left]] -= 1
                left += 1
        return ans