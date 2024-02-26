# 0076 - Minimum Window Substring
# Date: 2024-02-04
# Runtime: 67 ms, Memory: 17.3 MB
# Submission Id: 1165586643


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = len(t)
        
        table = {}
        for ch in t:
            table[ch] = table.get(ch, 0) + 1
        
        left = ans_left = ans_right = 0
        for right, ch in enumerate(s, 1):
            table[ch] = table.get(ch, 0) - 1
            if table[ch] >= 0:
                count -= 1
            if count == 0:
                while table[s[left]] < 0:
                    table[s[left]] += 1
                    left += 1
                if ans_right == 0 or ans_right - ans_left > right - left:
                    ans_left, ans_right = left, right
                table[s[left]] += 1
                left += 1
                count += 1
        return s[ans_left:ans_right]