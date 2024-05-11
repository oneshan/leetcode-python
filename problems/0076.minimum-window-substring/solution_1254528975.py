# 0076 - Minimum Window Substring
# Date: 2024-05-10
# Runtime: 98 ms, Memory: 17.3 MB
# Submission Id: 1254528975


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        size = len(t)

        left = 0
        ans_len, ans_left = float('inf'), 0
        for right, ch in enumerate(s):
            counter[ch] -= 1
            if counter[ch] >= 0:
                size -= 1
            if size > 0:
                continue
            while counter[s[left]] < 0:
                counter[s[left]] += 1
                left += 1
            if right - left + 1 < ans_len:
                ans_len = right-left+1
                ans_left = left

            counter[s[left]] += 1
            left += 1
            size += 1

        if ans_len == float('inf'):
            return ''
        return s[ans_left: ans_left + ans_len]