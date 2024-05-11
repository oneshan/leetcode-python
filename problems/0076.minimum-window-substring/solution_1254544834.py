# 0076 - Minimum Window Substring
# Date: 2024-05-10
# Runtime: 121 ms, Memory: 17.2 MB
# Submission Id: 1254544834


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        window = Counter()

        have, need = 0, len(counter)

        left = 0
        ans_left, ans_len = 0, float('inf')
        for right, ch in enumerate(s):
            window[ch] += 1
            if window[ch] == counter[ch]:
                have += 1
            
            if have != need:
                continue

            while have == need:
                window[s[left]] -= 1
                if window[s[left]] == counter[s[left]] - 1:
                    have -= 1
                    length = right - left + 1
                    if length < ans_len:
                        ans_left, ans_len = left, length
                left += 1

        if ans_len == float('inf'):
            return ''
        return s[ans_left:ans_left+ans_len]