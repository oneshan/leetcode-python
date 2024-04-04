# 2599 - Take K of Each Character From Left and Right
# Date: 2024-03-23
# Runtime: 265 ms, Memory: 17.4 MB
# Submission Id: 1211273909


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        counter = Counter(s)
        if not all(counter[ch] >= k for ch in 'abc'):
            return -1

        ans = left = 0
        for right, ch in enumerate(s):
            counter[ch] -= 1
            while counter[ch] < k:
                counter[s[left]] += 1
                left += 1
            ans = max(ans, right-left+1)
        return len(s) - ans