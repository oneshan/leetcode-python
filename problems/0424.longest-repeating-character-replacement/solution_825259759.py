# 0424 - Longest Repeating Character Replacement
# Date: 2022-10-18
# Runtime: 284 ms, Memory: 14 MB
# Submission Id: 825259759


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            table[s[right]] += 1
            curr_len = right - left + 1
            if curr_len - max(table.values()) <= k:
                ans = max(ans, curr_len)
            else:  # slide the window
                table[s[left]] -= 1
                left += 1
        return ans