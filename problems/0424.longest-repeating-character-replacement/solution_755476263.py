# 0424 - Longest Repeating Character Replacement
# Date: 2022-07-24
# Runtime: 196 ms, Memory: 14 MB
# Submission Id: 755476263


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {}
        left = ans = 0
        for right, ch in enumerate(s):
            table[ch] = table.get(ch, 0) + 1
            curr_len = right - left + 1
            if curr_len - max(table.values()) <= k:
                ans = max(ans, curr_len)
            else:  # slide the window
                table[s[left]] -= 1
                left += 1
        return ans