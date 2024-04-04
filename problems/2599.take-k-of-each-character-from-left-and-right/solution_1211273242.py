# 2599 - Take K of Each Character From Left and Right
# Date: 2024-03-23
# Runtime: 567 ms, Memory: 17.5 MB
# Submission Id: 1211273242


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        counter = Counter(s)
        if not all(counter[ch] >= k for ch in 'abc'):
            return -1

        res = n = len(s)
        left = length = 0
        for ch in s:
            counter[ch] -= 1
            length += 1
            while left < n and not all(counter[ch] >= k for ch in 'abc'):
                counter[s[left]] += 1
                left += 1
                length -= 1
            res = min(res, n-length)
        return res