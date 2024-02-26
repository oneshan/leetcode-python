# 0387 - First Unique Character in a String
# Date: 2022-07-17
# Runtime: 218 ms, Memory: 14.2 MB
# Submission Id: 748893158


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        for idx, ch in enumerate(s):
            if counter[ch] == 1:
                return idx
        return -1